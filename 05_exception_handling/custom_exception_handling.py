#In python, we can raise custom errors by using the raise keyword.


b=input("Enter a number:")



if   b.strip().lower() =="quit":
    print("Exiting....")
else:

    try:
        c=int(b)
        print(f"{c} is an integer {type(c)}") 
    except ValueError:
        raise ValueError(f"{b} is not a number or quit string")


