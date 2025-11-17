#Dictionary

info={"name":"Nishan","age":15,"address":"chabahil"
      
      }

print(info["name"])
print(info["age"])
print(info)


r=[info]
print(r)


print("All items from a dict",info.items())

#iterating items insid the dictionary


for key,value in info.items():
    print(f"{key} : {value}")


#doesnt gives error if not present it returns none
print(info.get("caste"))

#update can be done using update method

list={"caste":"khatri"}

info.update(list)
print(info)

#pop item method removes the last item key value pair 
#del will remove the whole dictionary


print(info.get("head","Not available"))

del info["name"]
print(info)

#.keys method will show all the keys 

print(info.keys())
print(info.values())