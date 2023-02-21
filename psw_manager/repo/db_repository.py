import sqlite3

PATH = ''
CONNECTION = None
CURSOR = None

def read() -> dict:
	result = CURSOR.execute('select resource, password from my_passwords', )
	return dict(result.fetchall())

def add(Resource) -> str:
	q = f'insert into my_passwords (resource, password) VALUES ("{Resource.resource}", "{Resource.password}");'
	CURSOR.execute(q)
	CONNECTION.commit()
	return 'Resource password successfully added'

def delete(Resource) -> str:
	return 'Resource password successfully deleted'	

def update(Resource, resource_old) -> str:
	return 'Resource update was successful'

def connect_db():
	global CONNECTION, CURSOR
	if CONNECTION == None:
		try:
			CONNECTION = sqlite3.connect(PATH)
			CURSOR = CONNECTION.cursor()
			CURSOR.execute('''CREATE TABLE IF NOT EXISTS my_passwords (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			resource TEXT NOT NULL,
			password TEXT NOT NULL
		);''')	
			CONNECTION.commit()
		except:
			print('Failed to connect to database. Check your connection string')
		