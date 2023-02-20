import psw_manager.repo.db_repository as db_repository
import psw_manager.repo.json_repository as json_repository
import psw_manager.config as config
from os.path import join, isfile, exists
from os import mkdir


if not exists(config.DIR_REPO):
    mkdir(config.DIR_REPO)


REPO = None
if config.TYPE_REPOSITORY == 'json':
    REPO = json_repository
    REPO.PATH = config.PATH_REPO
    if isfile(config.PATH_REPO) == False:
        with open(config.PATH_REPO, 'w') as filerepo:
            filerepo.write('{}')
elif config.TYPE_REPOSITORY == 'db':
    try:
        REPO = db_repository
        REPO.PATH = config.PATH_REPO
        REPO.connect_db()
    except KeyboardInterrupt as e:
        print(e)
