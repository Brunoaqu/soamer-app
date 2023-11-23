from client import get_client
from get_account_id import get_account_id

from random import randrange

status = [
    # "9", # Bloqueado
    "11", # A Fazer
    "2", # Corte | Ajuste 
    "3", # Molde | Expandir
    "4", # Solda | Rebarba
    "6", # Marcação | Furação
    "12", # Polimento | Remoção de Solda
    "7", # Polimento | Prep. Interna Rebarba
    "13", # Polimento | Prep. Externa
    "21", # Limpeza
    "8", # Pintura
    "5", # Embalagem
    "31", # Concluído
]

def choose_status():
    return randrange(len(status))

def move_issues_around():
    """
    Move issues randomly
    """
    jc          = get_client()
    issues      = jc.search_issues('project="PRJ"')

    for i in issues:
        choice = randrange(len(status))
        if (choice != 0): 
            pass
        
        for n in range(1, choice):
            jc.transition_issue(i, transition=status[n])

    jc.transition_issue(issues[0], transition="9") # type: ignore
    jc.transition_issue(issues[1], transition="9") # type: ignore
    jc.transition_issue(issues[2], transition="9") # type: ignore
    jc.transition_issue(issues[3], transition="31") # type: ignore

    childs = [
        "Montagem União Y", "Ajuste Dupla", "Rebarba Polimento", "Marmiteira", "Rebarba", "Macho", "Parafuso",
        "Soldagem União Y", "Rebate", "Remoção Solda", "Gel", "Lixa 80", "Feltro", "Etiqueta Externa",
        "Marcação", "Lixa 120", "Remoção Gel", "Gel", "Lavagem", "Etiqueta Externa",
        "Soldagem União AC", "Rastreio", "Lixa 220", "Cizal", "Polimento Final", "Secagem", "Embalagem",
        "Porqueamento", "Furação", "Lixa 320", "Limpeza Pano", "Fécula", "Revisão",
        "Solda Batente", "Rebarba Furação", "Decapagem", "Pedrinha", "Polimento Final", "Pano", "Revisão"
    ]

    for c in childs:
        child = jc.create_issue(
            project="PRJ",
            summary=c,
            issuetype={'name': 'subtarefa'},
            parent={'key': issues[3].key} # type: ignore
        )
        child.update(assignee=get_account_id())

move_issues_around()