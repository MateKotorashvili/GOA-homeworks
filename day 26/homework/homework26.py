# ; მომხმარებელს შეეკითხეთ სწავლობს თუარა 
# ; გოაში, თუ სწავლობს შეეკითხეთ ომელ ჯგუფშია, თუ პასუხი იქნება ჯგუფი13 
# ; შეეკითეთ რომ არის თუ არა გაბრიელი მისი 
# ; მენტორი, თუ პასუხი იქნება კი უთხარით რომ თქვენც 
# ; აქ სწავლობთ და ნამდვილად გაბრიელია ორივეს მენტორი, თუ პასუხი არიქნება გაბრიელი ყველა სხვა 
# ; შემთხვევაში დაუბეჭდეთ რომ ის 
# ; ტყუის და არარის სინამდვილეში ჯგუფ13-ში

question = input("do u study in GOA? yes/no:  ")
answer = "yes"
answer_two = "no"
answer_three = "yes"
answer_four = "13"
question_two = "in which group are you? :  "
question_three = "is your mentor Gabrieli? yes/no:  "

if question == answer:
    question_two = input("in which group are you? :  ")
    if question_two == answer_four:
        question_three = input("is your mentor Gabrieli? yes/no:  ")
        if question_three == answer:
            print("we are in the same group and our mentor is Gabriel molodin")
        else:
            print("you are lying cuse im in group 13 and my mentor is Gabrieli")
