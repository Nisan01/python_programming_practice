



#method to encode

def encode_message(message1):
 container=[]
 split_message=message1.split()
 
 for message in split_message:
        if(len(message)>3):
            
            r1="dlg"
            r2="pst"
            final_string=r1+message[1:]+message[0]+r2
        
        
            container.append(final_string)

        else:
            container.append(message[::-1])
 return(" ".join(container))







def message_decoding(message1):
    container=[]
    split_message=message1.split()
        
    for message in split_message:
        if(len(message)>3):

            remove_first_last=message[3:-3]
            remove_last_append=remove_first_last[-1:]+remove_first_last[:-1]
            container.append(remove_last_append)
            
           
          
        
       

        else:
            container.append(message[::-1])
    return(" ".join(container))        



message1=input("Enter your String: ")

select_option=input("Press E or encoding D for Decoding :")

if(select_option.lower()=="e"):
    s=encode_message(message1)
    print(f"Encoded Sting {s}")
    
    decoder_input_data=input("Do you want to decode it ? press 1 for yes 0 for exit : ")

    if(decoder_input_data.lower()=="1"):
       
        e=message_decoding(s)
        print(e)


elif(select_option.lower()=="d"):

    message_decoder=encode_message(message1)
    e=message_decoding(message_decoder)
    print(e)
    
else:
    print("---------ERROR----------------\n")
    print("---------Please type E or D only----------------")
 
       








    