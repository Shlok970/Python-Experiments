class Dog:
	species = "Labrador"
	def __init__(self, name, age):
		self.name = name
		self.age  = age
	def bark(self):
		return f"{self.name} barks : Woof! Woof!"
	def get_info(self):
		return f"{self.name} is a {self.age} year old {self.species}"
if __name__ == '__main__':
	dog1 = Dog("Buddy",3)
	dog2 = Dog("Lucy",5)
	print("\n ----Calling methods----")
	print(dog1.bark())
	print(dog2.bark())
	print("\n ----Object Information----")
	print(dog1.get_info())
	print(dog2.get_info())
	
		