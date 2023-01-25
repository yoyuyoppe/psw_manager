import json

PATH = ''
DATA = {}


def read() -> dict:
    global DATA

    with open(PATH, 'r') as f:
        DATA = json.load(f)

    return DATA


def add(Resource) -> str:
    if not DATA:
        read()

    with open(PATH, 'w') as f:
        DATA.update({Resource.resource: Resource.password})
        json.dump(DATA, f)

    return 'Resource password successfully added'


def delete(resource: str) -> str:
    if not DATA:
        read()

    if DATA.get(resource) is None:
        return f'Could not find resource {resource}'

    with open(PATH, 'w') as f:
        del DATA[resource]
        json.dump(DATA, f)

    return 'Resource password successfully deleted'


def update(Resource, resource_old) -> str:
    if not DATA:
        read()
    with open(PATH, 'w') as f:
        del DATA[resource_old]
        DATA.update({Resource.resource: Resource.password})
        json.dump(DATA, f)

    return 'Resource update was successful'
