
def get_by_number(number):
    match number:
        case 1:
            return("sunday")
        case 2:
            return("monday")
        case 3:
            return("tuesday")
        case _:
            return("saturday")
        



print(get_by_number(1))       


def prime_number_compare(pnumber):

    c=0

    
    for i in range(1,pnumber+1,1):
        if(pnumber % i == 0):
            c=c+1

    if c==2:
        return f"{pnumber} is prime"
    else:
        return f"{pnumber} is not prime"       

print(prime_number_compare(2))
        