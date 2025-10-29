#Program to take age and name from user and display it
name = input("Enter your name : ")
age_str = input("Please enter your age : ")
try:
	age = int(age_str)
except ValueError:
	print("Invalid age entered. Using a default age of 25.")
	age = 25
print(f"\nHello, {name}!")
years_to_100 = 100 - age
print(f"You will be 100 years old in {years_to_100}")