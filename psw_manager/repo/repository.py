from psw_manager.repo import REPO, config


def read() -> dict:
    data = {}
    if REPO is not None:
        data = REPO.read()
    else:
        data = {'data': [
            {'error': f'В настройках указан неизвестный тип репозитория {config.TYPE_REPOSITORY}'}]
		}

    return data


def add(Resource) -> str:
    data = ''
    if REPO is not None:
        data = REPO.add(Resource)
    else:
        data = f'В настройках указан неизвестный тип репозитория {config.TYPE_REPOSITORY}'

    return data


def delete(resource: str) -> str:
	data = ''
	if REPO is not None:
		data = REPO.delete(resource)
	else:
		data = f'В настройках указан неизвестный тип репозитория {config.TYPE_REPOSITORY}'
		
	return data


def update(Resource, resource_old) -> str:
	data = ''
	if REPO is not None:
		data = REPO.update(Resource, resource_old)
	else:
		data = f'В настройках указан неизвестный тип репозитория {config.TYPE_REPOSITORY}'
		
	return data
