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

# --- Helper function to display options ---
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
            
            # Ensure there is at least one wrong answer to pick from (should be 3)
            if wrong_options:
                # Select one random wrong answer
                fifty_fifty_list.append(random.choice(wrong_options))
            
            # 3. Shuffle the final two
            random.shuffle(fifty_fifty_list)
            
            # 4. Filter the original shuffled options to only show the two remaining
            # This is important because the user must still enter the index of the original 4 options
            final_options_to_display = fifty_fifty_list
            
            print("\n--- 50-50 Activated ---")
            display_options(final_options_to_display)
            
            print("Please enter the number corresponding to your choice in the original options (1, 2, 3, or 4).")
            # The input logic remains the same below, but the user is guided by the 50/50 display.
            
        elif user_lifeline_ans_str in ["1", "3"]:
            print(f"\n{life_lines[int(user_lifeline_ans_str) - 1]} activated (Simulated... pick your answer):")
            display_options(current_options)
        else:
            print("Invalid lifeline choice. Proceeding without lifeline.")
            display_options(current_options)


    # --- User Answer Input ---

    # We need to map the user's input (1, 2, 3, or 4) to the shuffled list.
    user_answer_str = input(f"Enter your Answer (1, 2, 3, or 4): ").strip()

    if not user_answer_str.isdigit() or int(user_answer_str) not in range(1, len(current_options) + 1):
        print("\nError\n------Please Enter a valid option number (1, 2, 3, or 4)------")
        break # End the game due to invalid input
    
    user_answer_index = int(user_answer_str) - 1
    
    # Check the answer against the shuffled list
    if current_options[user_answer_index].strip().lower() == correct_option_text.strip().lower():
        money_won = 10000 * (i + 1) # Simplified the multiplier for prizes
        print(f"\nRight Answer! You won ${money_won}")
        earned_money.append(money_won)
    else:
        print(f"\nIncorrect Answer. The correct answer was: {correct_option_text}")
        print("you lose")
        
        if earned_money:
            # The last successful amount is the safe amount
            safe_money = earned_money[-1] 
            print(f"You leave with ${safe_money}!!")
        else:
            print("You leave with $0!!")
        
        break # End the game

# --- Final Game Conclusion ---
else:
    # This 'else' runs only if the loop finishes normally (all questions answered)
    print("\n\n🎉 CONGRATULATIONS! You answered all questions!")
    print(f"Your final winnings are ${earned_money[-1] if earned_money else 0}")