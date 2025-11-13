#timetable greeting program

gettime=input("Enter the time in hrs followed by am or pm (5am)").strip().lower()


if gettime.endswith("am"):
    hour=int(gettime[:-2])
    period="am" 
elif gettime.endswith("pm"):
    hour=int(gettime[:-2])
    period="pm"
else:
    print("Invalid input")


if period == "am":
    print("Good Morning")
else:
    print("Good Afternoon")                