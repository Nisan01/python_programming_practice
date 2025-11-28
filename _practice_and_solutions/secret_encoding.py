# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode


import random
import string


message=input("Enter a word")
print("Before Encoding",message)

#message encoding 

random_characters="abcdefghijk"

if len(message)<3:
        print(message[::-1])
else:
    first_letter_store=message[:1]
    trimmed_word=message[1:]
    joinned_word=trimmed_word+first_letter_store
    
    random_string_start=''.join(random.choice(string.ascii_letters) for _ in range(3))
    random_string_end=''.join(random.choice(string.ascii_letters) for _ in range(3))
    
    secret_encoded_word=random_string_start+joinned_word+random_string_end
    print("secret word is ",secret_encoded_word)




#decoding time 

if len(secret_encoded_word)<3:
      print(secret_encoded_word[::-1] )
else:
      
      core_word = secret_encoded_word[3:-3]
      final_string=core_word[-1:]
      remove_last=core_word[:-1]

      final_string_decoded=final_string+remove_last
      print("After Decoding",final_string_decoded)  

   


   


