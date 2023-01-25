from psw_manager.repo import repository
import psw_manager.models.Resource as module_resource
from psw_manager.cryptomanager import encrypted, decrypted, generate_password


def showListPassword() -> str:
    data = repository.read()
    info = ''

    keys = data.keys()

    for k in keys:
        if k == 'error':
            info = f'error: {data.get(k)}'
        else:
            info += f'{module_resource.Resource(k, decrypted(data.get(k)))}\n'

    if info == '':
        info = 'Resource list is empty'

    return info


def create_password() -> str:
	return generate_password()


def add():
    resource = input('Input resource name: ')
    password = input('Input password for resource: ')
    newResource = module_resource.Resource(resource, encrypted(password))
    return repository.add(newResource)


def delete():
    resource = input('Input resource name: ')
    return repository.delete(resource)


def update() -> str:
	resource_old = input('Input old resource name: ')
	resource = input('Input resource new name: ')
	password = input('Input new password for resource: ')
	newResource = module_resource.Resource(resource, encrypted(password))
	return repository.update(newResource, resource_old) 	
