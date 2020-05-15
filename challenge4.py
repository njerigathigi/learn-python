#create a function that will accept a list of integers
#and remove duplicates.
#create a new list without duplicates

chores = ["dishes" ,"Laundry" ,"dishes" ,"Bathrooms" ,"laundry"]

def removedup(items):
    new_list = []
    for item in items:
        if item.casefold() in new_list:
            pass
        else:
            new_list.append(item.casefold())
    return new_list

print(removedup(chores))
