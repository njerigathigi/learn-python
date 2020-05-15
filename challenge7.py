employees = [{
  "id": 1,
  "first_name": "Winny",
  "last_name": "Waller",
  "email": "wwaller0@google.de",
  "gender": "Female",
  "name": "Winny Waller",
  "occupation": "Accounting Assistant II"
}, {
  "id": 2,
  "first_name": "Dud",
  "last_name": "Spur",
  "email": "dspur1@reuters.com",
  "gender": "Male",
  "name": "Dud Spur",
  "occupation": "Senior Quality Engineer"
}, {
  "id": 3,
  "first_name": "Ward",
  "last_name": "Gulliman",
  "email": "wgulliman2@washington.edu",
  "gender": "Male",
  "name": "Ward Gulliman",
  "occupation": "Analyst Programmer"
}, {
  "id": 4,
  "first_name": "Zach",
  "last_name": "Pratt",
  "email": "zpratt3@clickbank.net",
  "gender": "Male",
  "name": "Zach Pratt",
  "occupation": "Help Desk Technician"
}, {
  "id": 5,
  "first_name": "Daphene",
  "last_name": "Casburn",
  "email": "dcasburn4@ucsd.edu",
  "gender": "Female",
  "name": "Daphene Casburn",
  "occupation": "Product engineer"
}]


def get_names(employee_profiles):

    '''returns a list of employees' names '''
    
    names = []
    
    for profile in employee_profiles:
        if "name" in profile:
            names.append(profile["name"])
    return names  
               
    
    
        
# print(get_names(employees))

def get_engineers(employee_profiles):
    
    '''returns a list of the company's Engineers'''

    engineers = []
    
    for profile in employee_profiles:
        if "engineer" in profile["occupation"].casefold() :
            engineers.append(profile["name"])
    return engineers

print(get_engineers(employees))
