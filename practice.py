class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def print_name(self):
        print(self.name)

njeri = Employee('Fiona Njeri', 26, 500000)

# print(type(njeri))
print(njeri.name)
njeri.print_name()

harrison = Employee('Harrison Chege', 29, 1000000)
print(harrison.name)
harrison.print_name()
 