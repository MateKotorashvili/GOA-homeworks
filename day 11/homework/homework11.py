# მომხარებელს შემოატანინეთ მშობლების ასაკი, დედის და მამის ასაკი, შემდეგ თუ დედის ასაკი მეტი იქნება მამის ასაკზე
#         დაგვიბეჭდოს რომ დედა დიდი მამაზე, თუ პირიქით მამის ასაკი მეტი იქნება დედის ასაკზე მაგ შემთხვევაში დაგვიბეჭდოს 
#         რომ მამა დიდია დედაზე. მინიშნება დაგჭირდებათ (if)

mom_age = int(input("type your mom's age: "))
dad_age = int(input("type your dad's age: "))

if mom_age < dad_age:
    print("dad is older than mom")

if mom_age > dad_age:
    print("mom is older than dad")