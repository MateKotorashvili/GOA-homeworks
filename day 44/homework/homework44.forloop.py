#For Loop:

#1) Print all integers from 0 to 20 inclusive.

for i in range (0,21):
    print(i)

#2) Print the first 10 natural numbers.

for i in range (0,10):
    print(i)

#3) Print even numbers separately and odd numbers separately from 0 to 100 inclusive.
for i in range (0,100):
    if i % 2 == 0:
        print("the even is " + str(i))
    else:
        print("the odd is " + str(i))    
#4) Enter a number to the user and then using a for loop output the sum of all the numbers up to this number (for example, if he enters 10, output the sum of all the numbers up to 10, for example).
sum_of_numbers = 0
number = int(input("შეიყვანეთ რიცხვი: "))
for i in range(number):
    sum_of_numbers += i
print("რიცხვების ჯამი: " + str(sum_of_numbers))

#5) Write an algorithm that prints multiples of 5 (numbers divisible by 5) from 1 to 50 inclusive

for i in range(1, 51):
    if i % 5 == 0:
        print(i)
