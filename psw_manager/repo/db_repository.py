import sqlite3

PATH = ''
CONNECTION = None
CURSOR = None

def read() -> dict:
	return {}

def add(Resource) -> str:
	return 'Resource password successfully added'

def delete(Resource) -> str:
	return 'Resource password successfully deleted'	

def update(Resource, resource_old) -> str:
	return 'Resource update was successful'

def connect_db():
	global CONNECTION, CURSOR
	if CONNECTION == None:
		try:
			CONNECTION = sqlite3.connect('./psw_manager.db')
			CURSOR = CONNECTION.cursor()	
		except:
			print('Failed to connect to database. Check your connection string')
		