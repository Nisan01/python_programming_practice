import random


print("\n------KAUN----BANEGA---CROREPATI-------")
# name=input("Enter Your Name :")

questions_list = [
    {
        "question": "What is the capital city of Nepal?",
        "answer": "kathmandu",
        "options": ["pokhara", "lalitpur", "kathmandu", "biratnagar"]
    },

    {
        "question": "What is the smallest district of Nepal?",
        "answer": "Bhaktapur",
        "options": ["Bhaktapur", "Dolpa", "Rukum", "Morang"]
    },

    {
        "question": "What is the area of Nepal?",
        "answer": "181181sq.m",
        "options": ["100000sq.m", "181181sq.m", "200000sq.m", "150000sq.m"]
    },

    {
        "question": "What is the capital city of India?",
        "answer": "Delhi",
        "options": ["Mumbai", "Kolkata", "Delhi", "Chennai"]
    }
]


# print(questions_list[0]["Question 1:"])

# user_answer=input("Answer please:")

# if user_answer == questions_list[0]["Answer:"]:
#     print("Right Answer !!")
#     print("Congrats you won 50k :")

# print(questions_list[0]["Answer:"])


'''
print(len(questions_list))

for i in range(len(questions_list)):
    print(questions_list[i][f"Question {i+1}:"])
    user_answer=input("Answer =")
    if user_answer.strip().lower() == questions_list[i]["Answer:"].strip().lower():
        print(f"you won {10000 * (i+4)}")
    else:
        print(f"you loose")
        print(f"Your won this much")
        break    
'''

#with multiple choices 


earned_money=[]


print(len(questions_list))

for i in range(len(questions_list)):
    q=questions_list[i]
    print(f"\nQuestion {i+1} : {q["question"]}\n")

    options=q["options"].copy()
    random.shuffle(options)

    for ind,item in enumerate(options):
        print(f"Option{ind+1}:{item}",end="\t")

        if (ind +1) % 2 == 0:
            print(f"\n")

    

   

    user_answer1=input(f"\nAnswer: ")
    if not user_answer1.isdigit() or user_answer1 not in [1,2,3,4]:
            print("Error\n------Please Enter a valid options------")
            break
    else:    
        user_answer=int(user_answer1)
    
   

      
        if options[user_answer-1] == q["answer"]:
            print(f"you won {10000 * (i+4)}")
            earned_money.append(10000*(i+4))
            print(earned_money)
        else:
            print(f"you loose")
            if earned_money:
                print(f"You earned {earned_money[-1]} till now!!")
            else:
                print("You earned 0 till now!!")
                break 