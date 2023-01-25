class Resource():

	def __init__(self, resource: str = '', password: str = ''):
		self.resource = resource
		self.password = password


	def __str__(self) -> str:
		return f'{self.resource} : {self.password}'