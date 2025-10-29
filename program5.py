def safe_divide():
	print("---Safe Division Program---")
	try:
		numerator=int(input("Enter the numerator: "))
		denominator=int(input("Enter the denominator: "))
		result=numerator/denominator
		print(f"Result: {result}")
	
	except ValueError:
		print("Error,please enter a valid number")
	
	except ZeroDivisionError:
		print("Error,cannot divide by Zero")

	except Exception as e:
		print("Some Error occured")
safe_divide()
		