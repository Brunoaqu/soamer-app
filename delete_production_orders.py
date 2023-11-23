from client import get_client

def delete_all_issues():
    """
    Bulk create fake issues in project.
    """
    jc          = get_client()
    issues      = jc.search_issues('project="PRJ"')

    for i in issues:
        i.delete() # type: ignore

delete_all_issues()
    