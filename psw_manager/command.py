import psw_manager.manager as manager
import sys

ACTIONS = {
	'show': 'show me list of passwords',
	'add': 'add new password',
	'del': 'delete password',
	'new': 'generate new password',
	'update': 'update resource/password',
	'exit': 'exit the program'
}

def run_command(command: str, **kwargs):
	result = 'Operation completed successfully'
	if command == 'show':
		result = manager.showListPassword()
	elif command == 'add':
		result = manager.add()
	elif command == 'del':
		result = manager.delete()
	elif command == 'new':
		result = manager.create_password()
	elif command == 'update':
		result = manager.update()
	elif command == 'exit':
		print('Goodbuy!!!')
		sys.exit()

	print(result)