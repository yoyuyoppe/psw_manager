import sys
sys.path.insert(1, '../psw_manager/')
import psw_manager.manager as manager

def test_showListPassword():
	result = True
	try:
		manager.showListPassword()
	except:
		result = False
	assert result == True


def test_create_password():
	result = True
	new_pass = ''
	try:
		new_pass = manager.create_password()
	except:
		result = False
	assert result == True and new_pass != ''

