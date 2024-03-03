#მომხმარებელს შემოატანინეთ ორი რიცხვი, მისი ასაკი და მშობლის ასაკი,
#შემდეგ კი შეადარეთ ისინი ერთმანეთს


your_age = int(input("tell us your age:   "))
your_mom_or_dad_age = int(input("tell us your dad's or mom's age:   "))


print(str(bool(your_age > your_mom_or_dad_age)) + (" when > you are not older than you parent"))
print(str(bool(your_age < your_mom_or_dad_age)) + (" when < you are younger than you parent"))