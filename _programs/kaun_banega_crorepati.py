import random

print("\n------KAUN----BANEGA---CROREPATI-------")


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

life_lines = ["Phone-a-friend", "50-50", "Audience-poll"]
earned_money = []
lifeline_used = False 

# --- function to display options ---
def display_options(options_list):
    """Displays options in two columns."""
    for ind, item in enumerate(options_list):
        print(f"Option {ind+1}: {item}", end="\t")
        if (ind + 1) % 2 == 0:
            print() 
    print() 



for i in range(len(questions_list)):
    q = questions_list[i]
    print(f"\n--- Question {i+1} ---")
    print(f"{q['question']}")

  
    current_options = q["options"].copy()
    random.shuffle(current_options)
    
    
    correct_option_text = q["answer"]
    
    display_options(current_options)

    
    
    # Check if 50/50 has already been used
    if not lifeline_used:
        lifeline_answer = input("Do you want to use a lifeline (y/n)? ").lower().strip()
    else:
        lifeline_answer = 'n'
        print("50-50 Lifeline already used.")

    
    final_options_to_display = current_options # Start with all options

    if lifeline_answer == "y" and not lifeline_used:
        print("\nAvailable Lifelines:")
        for lifeline_index, option in enumerate(life_lines):
            print(f"{lifeline_index + 1}: {option}", end="\t")
        
        user_lifeline_ans_str = input("\nEnter Lifeline number (1, 2, 3): ").strip()
        
        if user_lifeline_ans_str == "2": # 50-50 logic
            
            # --- 50-50 Implementation ---
            lifeline_used = True
            
            # 1. Start with the correct answer
            fifty_fifty_list = [correct_option_text]
            
            # 2. Add ONE random WRONG answer
            wrong_options = [opt for opt in current_options if opt != correct_option_text]
            
        
            if wrong_options:
                # Select one random wrong answer
                fifty_fifty_list.append(random.choice(wrong_options))
            
            random.shuffle(fifty_fifty_list)
            
           
            final_options_to_display = fifty_fifty_list
            
            print("\n--- 50-50 Activated ---")
            display_options(final_options_to_display)
            
            print("Please enter the number corresponding to your choice in the original options (1, 2, 3, or 4).")
           
            
        elif user_lifeline_ans_str in ["1", "3"]:
            print(f"\n{life_lines[int(user_lifeline_ans_str) - 1]} activated (Simulated... pick your answer):")
            display_options(current_options)
        else:
            print("Invalid lifeline choice. Proceeding without lifeline.")
            display_options(current_options)


    user_answer_str = input(f"Enter your Answer (1, 2, 3, or 4): ").strip()

    if not user_answer_str.isdigit() or int(user_answer_str) not in range(1, len(current_options) + 1):
        print("\nError\n------Please Enter a valid option number (1, 2, 3, or 4)------")
        break 
    user_answer_index = int(user_answer_str) - 1
    
  
    if current_options[user_answer_index].strip().lower() == correct_option_text.strip().lower():
        money_won = 10000 * (i + 1) 
        print(f"\nRight Answer! You won ${money_won}")
        earned_money.append(money_won)
    else:
        print(f"\nIncorrect Answer. The correct answer was: {correct_option_text}")
        print("you lose")
        
        if earned_money:
           
            safe_money = earned_money[-1] 
            print(f"You leave with ${safe_money}!!")
        else:
            print("You leave with $0!!")
        
        break 


else:
    
    print("\n\n CONGRATULATIONS! You answered all questions!")
    print(f"Your final winnings are ${earned_money[-1] if earned_money else 0}")



#other way of writing this program !!    

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

