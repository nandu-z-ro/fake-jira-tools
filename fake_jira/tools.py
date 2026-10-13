"""Search, detail and update-status tools over the mock table.

Every function returns plain dicts shaped like Jira Cloud REST v3 responses.
Unknown keys or statuses return Jira's error body instead of None or raising.
"""

from fake_jira.issues import COMPONENTS, ISSUES, STATUS_CATEGORIES

_BY_KEY = {row["key"]: row for row in ISSUES}


def _error(message: str) -> dict:
    return {"errorMessages": [message], "errors": {}}


def _not_found() -> dict:
    return _error("Issue does not exist or you do not have permission to see it.")


def _status(name: str) -> dict:
    return {"name": name, "statusCategory": {"key": STATUS_CATEGORIES[name]}}


def _components(names: list[str]) -> list[dict]:
    return [{"id": COMPONENTS[n], "name": n} for n in names]


def _issue_head(row: dict) -> dict:
    return {"id": row["id"], "key": row["key"], "self": f"/rest/api/3/issue/{row['id']}"}


def search_issues(
    project: str | None = None,
    component: str | None = None,
    status: str | None = None,
    text: str | None = None,
    max_results: int = 50,
) -> dict:
    """Filter issues, newest first. Mirrors GET /rest/api/3/search/jql."""
    hits = [
        row for row in ISSUES
        if (project is None or row["key"].split("-")[0] == project)
        and (component is None or component in row["components"])
        and (status is None or row["status"] == status)
        and (text is None or text.lower() in row["summary"].lower())
    ]
    hits.sort(key=lambda r: r["created"], reverse=True)
    issues = [
        {
            **_issue_head(row),
            "fields": {
                "summary": row["summary"],
                "status": _status(row["status"]),
                "components": _components(row["components"]),
            },
        }
        for row in hits[:max_results]
    ]
    return {"startAt": 0, "maxResults": max_results, "total": len(hits), "issues": issues}


def get_issue(key: str) -> dict:
    """Return one issue. Mirrors GET /rest/api/3/issue/{key}."""
    row = _BY_KEY.get(key)
    if row is None:
        return _not_found()
    assignee = {"displayName": row["assignee"]} if row["assignee"] else None
    return {
        **_issue_head(row),
        "fields": {
            "summary": row["summary"],
            "status": _status(row["status"]),
            "priority": {"name": row["priority"]},
            "components": _components(row["components"]),
            "assignee": assignee,
            "created": row["created"],
            "description": row["description"],
        },
    }


def update_status(key: str, status: str) -> dict:
    """Move an issue to a new status.

    Real Jira returns 204 with no body, so this returns the key and the
    status as it now reads, like the capture's follow-up GET.
    """
    row = _BY_KEY.get(key)
    if row is None:
        return _not_found()
    if status not in STATUS_CATEGORIES:
        return _error(f"Transition to '{status}' is not valid for this issue.")
    row["status"] = status
    return {"key": key, "fields": {"status": _status(status)}}
