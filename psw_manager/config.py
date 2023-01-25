import tempfile
from os.path import join, isfile

# json or db
TYPE_REPOSITORY = 'json'
PATH_REPO = join(tempfile.gettempdir(), f'psw_manager.{TYPE_REPOSITORY}')
#print(PATH_REPO)
