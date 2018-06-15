"""Examples of the factory  and singleton pattern in python."""

class Vehicle(object):
	'''Factory method helps with the problem of creating objects 
		without knowing exact class of the object that will be created.
	'''
	@staticmethod
	def factory(type):
		if type == 'car':
			return Car()
		if type == 'boat':
			return Boat()
		raise AssertionError('type not found: ', type)
	# factory = staticmethod(factory)

class Car(Vehicle):
	def drive(self):
		return 'vroom vroom'

class Boat(Vehicle):
	def drive(self):
		return 'splish splash'

class Singleton():
	'''Singleton class ensures only one instance is ever created.'''
	instance = None
	class __Singleton():
		'''The first time you create an OnlyOne, it initializes 
			instance, but after that it just ignores you.'''
		def __init__(self, arg):
			self.val = arg
		def __str__(self):
			return repr(self) + self.val
	
	def __init__(self, arg):
		if not Singleton.instance:
			Singleton.instance = Singleton.__Singleton(arg)
		else:
			Singleton.instance.val = arg
	def __getattr__(self, name):
		return getattr(self.instance, name)

def main():
	# Factory.
	v = Vehicle.factory('car')
	assert v.drive() == 'vroom vroom'
	v = Vehicle.factory('boat')
	assert v.drive() == 'splish splash'

	# Singleton.
	h = Singleton('hummingbird')
	print h
	b = Singleton('blackbird')
	print b
	r = Singleton('raven')
	print r
	

if __name__ == '__main__':
	main()