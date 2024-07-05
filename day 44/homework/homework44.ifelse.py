#If - Else:

#1) Write an if-else statement that prints "Good morning!" if the current hour is less than 12 and "Good afternoon!" otherwise.

time = int(input("please enter the time(12;01x. 12v/ 1x. 13v):  "))
if time < 12:
    print("good morning")
else:
    print("good afternoon")
#2) Write an if-else statement that checks if a number is even or odd. If the number is even, print "Even"; otherwise, print "Odd."

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number," is Even.")
else:
    print(number, "is Odd.")

#3) Create an if-else statement to check if the temperature is above 30 degrees. If it is, print "It's hot outside!"; otherwise, print "It's not too hot."

temperature = int(input("enter temperature:"))
if temperature < 30:
    print("its not too hot")
else:
    print("its hot outside!")    

#4) Create an if-else statement that determines if a person is a teenager. If the age is between 13 and 19 (inclusive), print "You are a teenager!"; otherwise, print "You are not a teenager."     

age = int(input("enter your age:  "))
if 13 < age < 19:
    print("you are a teenager")
else:
    print("you are not a teenager")