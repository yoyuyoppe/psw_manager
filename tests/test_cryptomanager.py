import sys
sys.path.insert(1, '../psw_manager/')
import psw_manager.cryptomanager as cryptomanager

def test_encrypted():
	result = True
	pswd = ''
	try:
		pswd = cryptomanager.encrypted('123456')
		result = True
	except:
		result = False
	assert result == True and pswd == '2468:<'


def test_decrypted():
	result = True
	pswd = ''
	try:
		pswd = cryptomanager.decrypted('2468:<')
	except:
		result = False
	assert result == True and pswd == '123456'


def test_generated_password():
	result = True
	try:
		pswd = cryptomanager.generate_password()
	except:
		result = False
	assert result == True
