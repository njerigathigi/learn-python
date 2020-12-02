# A dictionary can contain dictionaries, this is called nested dictionaries.



myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for person in myfamily:
    print('{0} is {1} born in the year {2}.'
          .format(person, myfamily[person]['name'], myfamily[person]['year']))



# Create three dictionaries, then create one dictionary that will contain the other 
# three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print()

for person in myfamily:
    print('{0} is {1} born in {2}.'
         .format(person , myfamily[person ]['name'],myfamily[person ]['year']))
