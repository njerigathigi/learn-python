class Customer:
    def __init__(self, name, membership_type): #self refers to the current instance of the class.
        self.name = name
        self.membership_type = membership_type
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        print('setting name')
        self._name = name

    def update_membership(self, new_membership):
        print('calculating cost')
        self.membership_type = new_membership
    
    @staticmethod #decorator
    def read_customer(): #static method
        print('Reading customer from DB')

    def __str__(self): # The __str__ method is useful for a string representation of the object.
        print('converting to string')
        return self.name + ' ' + self.membership_type
    
    @staticmethod
    def print_all_customers(customers):
        for customer in customers:
            print(customer)
    
    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True

        return False

    __hash__ =  None
    __repr__ = __str__


    

# c = Customer('caleb', 'gold')
# print(c.name)
# print(c.membership_type)
# c2 = Customer('Brad', 'Bronze')
# print(c2.name, c2.membership_type)

# customers = [c, c2] #not scalable
# print(customers) 

customers = [
    Customer('Caleb', 'Gold'),
    Customer('Brad', 'Bronze'),
    ]
# print(customers[0].name, customers[0].membership_type)
# print()
# print(customers[1].membership_type)
# customers[1].update_membership('Gold')
# print(customers[1].membership_type)
# customers[1].membership_type = 'Bronze'
# print(customers[1].membership_type)

# customers[1].verified = False #you can assign attributed after __init__
# print(customers[1].verified)
# print(customers[0].verified) #raises an error

# customers[1].read_customer() #raises a type error #cannot invoke it on an object but you can 
#invoke it on the class. ie has nothing to do with an individual customer
# read_customer() is a static method. its not attached to any indivual object but can be invoked 
#on the class itself.
# Customer.read_customer()

Customer.print_all_customers(customers)

print(customers[0] == customers[1]) #testing __eq__() method
