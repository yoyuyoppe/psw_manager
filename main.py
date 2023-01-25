from psw_manager import command, ACTIONS

if __name__ == '__main__':
	print('Welcome to the password manager\nEnter action code:')

	for action in ACTIONS:
		print(f'{action}: {ACTIONS.get(action)}')

	while True:
		action_code = input('Action code: ')
		print('')
		if ACTIONS.get(action_code) is None:
			print(f'Action code ({action_code}) not found')
		else:
			command.run_command(action_code)