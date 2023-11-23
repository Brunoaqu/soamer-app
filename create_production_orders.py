from jira import User
from client import get_client
from utils.synthesize import build_data

import json

childs = [
    "Montagem União Y", "Ajuste Dupla", "Rebarba Polimento", "Marmiteira", "Rebarba", "Macho", "Parafuso",
    "Soldagem União Y", "Rebate", "Remoção Solda", "Gel", "Lixa 80", "Feltro", "Etiqueta Externa",
    "Marcação", "Lixa 120", "Remoção Gel", "Gel", "Lavagem", "Etiqueta Externa",
    "Soldagem União AC", "Rastreio", "Lixa 220", "Cizal", "Polimento Final", "Secagem", "Embalagem",
    "Porqueamento", "Furação", "Lixa 320", "Limpeza Pano", "Fécula", "Revisão",
    "Solda Batente", "Rebarba Furação", "Decapagem", "Pedrinha", "Polimento Final", "Pano", "Revisão"
]

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

    for s in synthesized:
        issue = jc.create_issue(fields=s)
        issue.update(assignee=fields["assignee"])

        # Add Childs to Parent
        for c in childs:
            child = jc.create_issue(
                project="PRJ",
                summary=c,
                issuetype={'name': 'subtarefa'},
                parent={'key': issue.key}
            )
            child.update(assignee=fields["assignee"])

create_issue()
