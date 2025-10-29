import math
import random
import datetime
import os
print(f"---1.Using the maths module---")
print(f"The value of pi is {math.pi}")
print(f"The value cosine of pi is {math.cos(math.pi)}")
print(f"The square root of pi is: {math.sqrt(64)}")
print(f"\n---2.Using the random module----")
random_number = random.randint(1,10)
print(f"The random number between 1 and 10 is: {random_number}")
choices=['rock','paper','scissor']
random_choices=random.choice(choice)
print(f"The random choices from the first is: {random_choice}")
print("\n---3.Using the daytime module---")
current_date=datetime.data.today()
print(f"Today's date: {current_date}")
now=datetime.datetime.now()
print(f"The current date and time is: {now.strftime('%Y:%m:%d %d %H:%M:%S')}")
print("---4.Using the os module---")
curr_dir=os.getcwd()
print(f"The Current dictonary is: {curr_dir}")