import psw_manager.manager as manager
import sys

ACTIONS = {
	'0': 'show me list of passwords',
	'1': 'add new password',
	'2': 'delete password',
	'3': 'generate new password',
	'4': 'update resource/password',
	'exit': 'exit the program'
}

def run_command(command: str, **kwargs):
	result = 'Operation completed successfully'
	if command == '0':
		result = manager.showListPassword()
	elif command == '1':
		result = manager.add()
	elif command == '2':
		result = manager.delete()
	elif command == '3':
		result = manager.create_password()
	elif command == '4':
		result = manager.update()
	elif command == 'exit':
		print('Goodbuy!!!')
		sys.exit()

	print(result)