
#py program to count words,characters and sentence

import re

string1=" Hello how are you ? Are you fine."

print(f"Total no of Words:{len(string1.split())}")

char_fltr=string1.replace(" ","").replace("/n","")

print(f"Total no of characters:{len(char_fltr)}")



sentence_extract=re.split(r'[.!?]',string1)
sentences = [s for s in sentence_extract if s.strip()]
print(sentences)
print(sentence_extract)