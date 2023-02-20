import tempfile
from os.path import join, isfile

# json or db
TYPE_REPOSITORY = 'db'
#PATH_REPO = join(tempfile.gettempdir(), f'psw_manager.{TYPE_REPOSITORY}')
DIR_REPO = './db'
PATH_REPO = f'{DIR_REPO}/psw_manager.{TYPE_REPOSITORY}'
#print(PATH_REPO)
