class Student:
    def __init__(self, name):
        self.name=name
    def print_name(self):
        print(self.name)
    def print_upper(self):
        print(self.name.capitalize())
class Class(Student):
    pass

a=Student("raju")
a.print_name()
a.print_upper()