numbers = [11, -23, 2, 89, -19, 99, 7, -1]
negative_num = []
positive_num = []

for num in numbers:
    if num > 0:
        positive_num.append(num)
    elif num < 0:
        negative_num.append(num)
print("Positive numbers:", negative_num)
print("Negative numbers:", positive_num)

everynumber = negative_num + positive_num
print(everynumber)