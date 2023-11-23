from jira import User
from client import get_client

def get_account_id():    
    """
    Retrieve Account Id
    """
    jc = get_client()
    
    params = {
            "query": "bruno.gl.aquino+soamerprojeto@gmail.com",
            "includeActive": True,
            "includeInactive": False
    }
    list_search = jc._fetch_pages(
        item_type=User,
        items_key=None,
        request_path="user/search",
        params=params
    )

    jira_user_id = list_search[0].accountId
    fields = {"assignee": {"accountId": jira_user_id}}

    return fields["assignee"]