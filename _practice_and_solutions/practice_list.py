list_of_questions = [
    ["What is the capital city of Nepal?", "Mongolia", "Nepal", "Uruguay", "Kathmandu", "Kathmandu"],
    
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", "Mars"],
    
    ["Who wrote the Ramayana?", "Valmiki", "Veda Vyasa", "Tulsidas", "Kalidas", "Valmiki"],
    
    ["What gas do plants absorb from the atmosphere?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", "Carbon Dioxide"],
    
    ["Which is the largest ocean on Earth?", "Indian", "Pacific", "Atlantic", "Arctic", "Pacific"],
    
    ["Who discovered gravity?", "Edison", "Einstein", "Newton", "Tesla", "Newton"],
    
    ["What is the national animal of Nepal?", "Tiger", "Cow", "Rhino", "Lion", "Cow"],
    
    ["Which is the smallest prime number?", "1", "2", "3", "5", "2"],
    
    ["What is H₂O commonly known as?", "Salt", "Water", "Hydrogen", "Oxygen", "Water"],
    
    ["Which country invented paper?", "India", "China", "Japan", "Egypt", "China"]
]


print(list_of_questions[0])
q=list_of_questions[0]
print(q[1])
print(list_of_questions[0][1])

kbc_prize = [
    1000,          # Q1
    2000,          # Q2
    3000,          # Q3
    5000,          # Q4
    10000,         # Q5  (First Safe Level)
    20000,         # Q6
    40000,         # Q7
    80000,         # Q8
    160000,        # Q9
    320000      # Q10 (Second Safe Level)
         # Q15 (Crorepati Prize)
]

take_on_money=0


for i in range(len(list_of_questions)):
    q=list_of_questions[i]
    print(f"{q[0]}\n")
    print(f"A:{q[1]} \t B:{q[2]}")
    print(f"C:{q[3]} \t D:{q[4]}")

    response=input(f"Answer(Press 0 for quit)")

    if i == 4:
        take_on_money=10000
    elif i == 9:
        take_on_money=320000     

    if response.strip().lower() == q[-1].strip().lower():
        print(f"\nCorrect Answer")
        print(f"You won {kbc_prize[i]}\n")
    
    elif response == "0":
         print(f"You won {kbc_prize[i-1]} till now !!")
         break

    else:
        print("---------------Wrong Answer:-----------------")
    
        print(f"You take Rs{take_on_money} home !!")  
        break

