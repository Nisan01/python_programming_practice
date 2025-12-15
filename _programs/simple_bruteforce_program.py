import string


lower_string=string.ascii_lowercase
print(lower_string)
print(type(lower_string))


full_str=string.ascii_letters
print(full_str)


digits_checker=string.digits
special_character_checker=string.punctuation


password=input(f"Enter a password to crack !! :\n")

cracked=""
digit_loop_runner=True
punctuation_loop_runner=True

print("---------------------CRACKING-STARTED-----------------------------")

for p1 in password:
    if(p1.isalpha()):
        print(f"Checking for {p1} in alphabets")
        for f in full_str:
            if f==p1:
             cracked+=f
             print(f"character {f} found:")
             break
    

       
    elif(p1.isdigit()):
  
        print(f"Checking for {p1} in digits")
        for d in digits_checker:
         if d==p1:
            cracked+=d
            print(f"digit {d} found:")

            break
    else:
        print(f"Checking for {p1} in punctuation")
        for e in special_character_checker:
         if e==p1:
            cracked+=e
            print(f"Special Char {e} found:")
            break
           

     
print("--------------------CRACKED-PASSWORD-------------------------------")
print(cracked)
     




