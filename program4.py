def demonstrate_for_loop():
	print("---1.Using a for loop---")
	fruits=["apple",'banana',"cherry"]
	print("Iterating through a list of fruits")
	for fruit in fruits:
		print(f"-{fruits}")
	print("\nIterating through a range of 0 to 4:")
	for i in range(5):
		print(f"count:{i}")
def demonstrate_while_loop():
	print("\n---2.Using a while loop---")
	count=0
	print("\nCounting upto 5")
	while count<5:
		print(f"count is {count}")
		count+=1
	print("Example of break: ")
	for num in range(10):
		if num==5:
			print(f"Found 5 breaking the loop")
			break
			print(f"processing number: {num}")
	print("Example of continue: ")
	for num in range(10):
		if num==5:
			print(f"Found 5 continuing the loop")
			continue
		print(f"Processing number: {num}")
demonstrate_for_loop()
demonstrate_while_loop()