# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# reversed_numbers = list(reversed(numbers))
# print(reversed_numbers)

# numbers_two = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# reversed_numbers_two = []
# for i in range (len(numbers_two)):
#     reversed_numbers_two.append(numbers_two[-i-1])
# print(reversed_numbers_two)

numbers = [6, 5, 3, 10, 23, 25, 55, 16]
divide_five = []
for i in range(len(numbers)):
    if numbers[i] % 5 == 0:
        print(numbers[i])
