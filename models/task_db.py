tasks = [
    {'id': 1, 'title': 'Ir ao supermercado', 'done': False},
    {'id': 2, 'title': 'Estudar programação', 'done': False},
    {'id': 3, 'title': 'Atualizar o LinkedIn', 'done': False},
]

def newId():
    if len(tasks) == 0:
        return 1
    return max(task['id'] for task in tasks) + 1