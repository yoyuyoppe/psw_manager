import sys
sys.path.insert(1, '../psw_manager/')
import psw_manager.repo.repository as repository
import psw_manager.models.Resource as resource

testResource = resource.Resource('testResource', '123456')

def test_read():
	result = True
	try:
		repository.read()
	except:
		result = False
	assert result == True

def test_add():
	result = True
	try:
		result = repository.add(testResource)
	except:
		result = False
	assert result == 'Resource password successfully added'

def test_update():
	result = True
	old_resource = testResource.resource
	testResource.password = ''
	try:
		result = repository.update(testResource, old_resource)
	except:
		result = False
	assert result == 'Resource update was successful'

def test_delete():
	result = True
	try:
		result = repository.delete(testResource.resource)
	except:
		result = False
	assert result == 'Resource password successfully deleted'