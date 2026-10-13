"""Mock issue table. Each row is stored flat; tools.py builds the Jira shapes."""

# Status name -> Jira statusCategory key.
STATUS_CATEGORIES = {
    "To Do": "new",
    "In Progress": "indeterminate",
    "In Review": "indeterminate",
    "Done": "done",
}

# Component name -> component id.
COMPONENTS = {
    "Label Classifier": "10201",
    "Duplicate Detector": "10202",
    "Routing Engine": "10203",
    "Trace Viewer": "10204",
}

ISSUES = [
    {
        "id": "10412", "key": "TRIAGE-184",
        "summary": "Triage bot applied 'billing' label to an SSO login failure",
        "status": "In Progress", "priority": "High",
        "components": ["Label Classifier", "Trace Viewer"],
        "assignee": "Priya Venkataraman",
        "created": "2024-08-14T09:22:41.318+1000",
        "description": "Bot chose the label from the ticket title alone; "
        "the SSO error body was never read.",
    },
    {
        "id": "10398", "key": "SUPPORT-77",
        "summary": "Duplicate detection marks reopened tickets as duplicates of themselves",
        "status": "To Do", "priority": "Medium",
        "components": ["Label Classifier", "Duplicate Detector"],
        "assignee": None,
        "created": "2024-08-09T14:05:12.004+0530",
        "description": "Reopening a ticket links it to itself as a duplicate.",
    },
    {
        "id": "10405", "key": "TRIAGE-179",
        "summary": "Label classifier ignores non-English ticket bodies",
        "status": "To Do", "priority": "High",
        "components": ["Label Classifier"],
        "assignee": "Liam O'Connor",
        "created": "2024-08-12T11:40:03.551+1000",
        "description": "Japanese and Hindi tickets always get the 'general' label.",
    },
    {
        "id": "10391", "key": "TRIAGE-171",
        "summary": "Routing engine sends P1 outages to the low-priority queue",
        "status": "Done", "priority": "Highest",
        "components": ["Routing Engine"],
        "assignee": "Priya Venkataraman",
        "created": "2024-08-05T08:15:27.910+1000",
        "description": "Priority field was read before the classifier set it.",
    },
    {
        "id": "10387", "key": "SUPPORT-71",
        "summary": "Trace viewer drops tool results longer than 4 KB",
        "status": "In Review", "priority": "Medium",
        "components": ["Trace Viewer"],
        "assignee": "Arjun Mehta",
        "created": "2024-08-02T16:48:55.120+0530",
        "description": "Long tool outputs are cut, so runs cannot be replayed.",
    },
    {
        "id": "10380", "key": "SUPPORT-66",
        "summary": "Label classifier tags refund requests as 'shipping'",
        "status": "In Progress", "priority": "Medium",
        "components": ["Label Classifier"],
        "assignee": "Arjun Mehta",
        "created": "2024-07-30T10:02:44.731+0530",
        "description": "Refund wording overlaps with shipping keywords.",
    },
    {
        "id": "10376", "key": "TRIAGE-165",
        "summary": "Duplicate detector merges tickets from different customers",
        "status": "To Do", "priority": "High",
        "components": ["Duplicate Detector"],
        "assignee": None,
        "created": "2024-07-28T13:21:09.402+1000",
        "description": "Matching uses summary text only, not the customer id.",
    },
    {
        "id": "10369", "key": "TRIAGE-160",
        "summary": "Routing engine retries forever when the identity queue is full",
        "status": "In Progress", "priority": "High",
        "components": ["Routing Engine"],
        "assignee": "Liam O'Connor",
        "created": "2024-07-24T09:55:31.008+1000",
        "description": "No backoff or retry cap on queue-full responses.",
    },
    {
        "id": "10362", "key": "SUPPORT-58",
        "summary": "Trace viewer shows timestamps in UTC only",
        "status": "Done", "priority": "Low",
        "components": ["Trace Viewer"],
        "assignee": "Meera Iyer",
        "created": "2024-07-19T17:30:00.000+0530",
        "description": "Agents in Bengaluru asked for local time.",
    },
    {
        "id": "10355", "key": "SUPPORT-52",
        "summary": "Label classifier confidence score missing from bot comment",
        "status": "Done", "priority": "Low",
        "components": ["Label Classifier", "Trace Viewer"],
        "assignee": "Meera Iyer",
        "created": "2024-07-15T12:12:12.120+0530",
        "description": "The comment posts the label but not how sure the bot was.",
    },
    {
        "id": "10348", "key": "TRIAGE-152",
        "summary": "Routing engine assigns tickets to people on leave",
        "status": "In Review", "priority": "Medium",
        "components": ["Routing Engine"],
        "assignee": "Priya Venkataraman",
        "created": "2024-07-10T07:45:18.666+1000",
        "description": "Leave calendar is not checked before assignment.",
    },
    {
        "id": "10341", "key": "SUPPORT-45",
        "summary": "Duplicate detector misses tickets that differ only in casing",
        "status": "To Do", "priority": "Low",
        "components": ["Duplicate Detector"],
        "assignee": "Arjun Mehta",
        "created": "2024-07-06T15:03:27.333+0530",
        "description": "'SSO Login' and 'sso login' are treated as different.",
    },
]
