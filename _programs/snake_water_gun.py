import pyttsx3,random

engine=pyttsx3.init()

def game_function(user, system):
    # Draw
    if user == system:
        return 0
    
    # Win conditions
    elif (user == 1 and system == 2) or \
         (user == 2 and system == 3) or \
         (user == 3 and system == 1):
        return 1
    else:
        return -1


try:
    user = int(input('Enter your choice:\n1 Snake\n2 Water\n3 Gun\n'))
    
    if user not in [1, 2, 3]:
        raise ValueError

    systemInput = random.randint(1, 3)

except ValueError:
    print("❌ Enter a valid number (1, 2 or 3)")
    exit()


# Mapping values to names
data_map = ["Snake", "Water", "Gun"]

print("You chose:", data_map[user-1])
print("System chose:", data_map[systemInput-1])

result = game_function(user, systemInput)

if result == 0:
    c="Its a draw"
    print(c)
    engine.say(c)
    engine.runAndWait()

elif result == 1:
    c="You won!!"
    print(c)
    engine.say(c)
    engine.runAndWait()
else:
    c="You loose !!"
    print(c)
    engine.say(c)
    engine.runAndWait()
