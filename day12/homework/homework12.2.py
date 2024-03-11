# მოსწავლეს შემოატანინეთ სკოლის ტესტში მიღებული ნიშანი, თუ ეს მიღებული ნიშანი უდრის 10 - ს,
# მაგ შემთხვევაში მასწავლებელმა, მშობელთან შეაქოს მოსწავლე, თუ მიღებული ნიშანი უდრის 8 -ს ან 9 - ს,
# მაგ შემთხვევაში, მასწავლებელმა, მშობელს პატარა შენიშვნა მისცეს. თუ მიღებული ქულა უდრის 5  - ს მაგ შემთხვევაში,
# მასწავლებელმა, მშობელს მისცეს შენიშვნა,
# ხოლო თუ მიღებული ნიშანი ნაკლებია 5 ზე, მაგ შემთხვევაში, მასწავლებელმა გააგდოს მოსწავლე სკოლიდან

score = int(input("Type in your school test score:  "))

if score == 10:
    print("Your Teacher Told Your Parents That You Are a Very Good Student")
elif score == 9 or 8:
    print("Your Teacher Told Your Parents That You Are a Good Sudent But You Could Do It Better")
elif score == 5:
    print("Your Teacher Told Your Parents That You Are Did Bad In Your Test")
else :
    print("Your Teacher Kicked You Out Of School")