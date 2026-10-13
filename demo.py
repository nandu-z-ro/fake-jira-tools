"""Call each fake Jira tool once and print the result as JSON."""

import json

from fake_jira import get_issue, search_issues, update_status


def show(title: str, result: dict) -> None:
    print(f"=== {title} ===")
    print(json.dumps(result, indent=2))
    print()


show("search_issues(component='Label Classifier')", search_issues(component="Label Classifier"))
show("get_issue('TRIAGE-184')", get_issue("TRIAGE-184"))
show("update_status('SUPPORT-77', 'In Progress')", update_status("SUPPORT-77", "In Progress"))
