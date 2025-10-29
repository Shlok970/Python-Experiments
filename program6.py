class animal:
	def __init__(self,name):
		self.name=name

	def speak(self):
		raise NotImplementedError("subclass must implement abstract method")
		
class dog(animal):
	def speak(self):
		return "Woof!"
class cat(animal):
	def speak(self):
		return "Meow!"
def make_it_speak(animal):
	print(f"{animal.name} says {animal.speak()}")
if __name__=="__main__":
	dog1=dog("Bruno")
	cat1=cat("whiskey")
	print("\n1---Demonstrating inheritance---")	
	print(f"My dog's name is {dog1.name}")
	print(f"My cat's name is {cat1.name}")
	print("\n2---Demonstrating polymorphism---")
	make_it_speak(dog1)
	make_it_speak(cat1)