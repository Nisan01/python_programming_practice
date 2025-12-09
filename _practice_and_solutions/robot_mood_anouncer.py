
import pyttsx3,random

engine=pyttsx3.init()

feelings=[
    "I am a powerful robot",
    "I am made to colonize human beings !!",
    "Hey , I can kill you",
    "I am untouchable",
    "SUch a pity human beings haahaa"
]


mood1=random.choice(feelings)
finalString=f"Hey ..I am Xarvis \n"+mood1

print(f"--------------Robot Speaks--------------\n"+finalString)

engine.say(finalString)
engine.runAndWait()



