from client import get_client
from get_account_id import get_account_id
from utils.synthesize import build_data

import json

def js_r(filename: str):
    """
    Parse Mock File
    """
    with open(filename) as f_in:
        return json.load(f_in)

def create_issue():
    """
    Bulk create fake issues in project.
    """
    build_data(40)
    
    synthesized = js_r("./test/sample.json")
    jc          = get_client()

    for s in synthesized:
        issue = jc.create_issue(fields=s)
        issue.update(assignee=get_account_id())

create_issue()
