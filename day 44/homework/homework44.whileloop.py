# While Loop:

#1) Print even numbers up to 20.

num = 0
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1
#2) calculate the sum of numbers from 1 to 10.

i = 0
total_sum = 0

while i <= 10:  
    total_sum += i
    i += 1

print("The sum of numbers from 1 to 10 is:" + str(total_sum))

#3) Write a while loop that asks the user to guess a number between 1 and 10 until they get it right. The correct number is 7.

correct_answer = 7
question = int(input("enter number from 1 to 10:  "))
while question != correct_answer:
    print("try again")
    question = int(input("enter number from 1 to 10:  "))
print("you gess the number finally")

#4) Write a while loop that processes a list of numbers, doubling each number, and prints the new list.

numbers = [1, 2, 3, 4, 5]
doubled_numbers = []
index = 0

while index < len(numbers):
    doubled_numbers.append(numbers[index] * 2)
    index += 1

print("Doubled numbers:", doubled_numbers)

#5)Write a while loop that repeatedly asks the user to enter a password until the correct password "password123" is entered.

correct_password = "password123"
password_question = input("enter password:  ")

while password_question != correct_password:
    print("incorect")
    password_question = input("enter password:  ")
else:
    print("correct!come in.")