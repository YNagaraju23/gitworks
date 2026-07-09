class Parent:
    def __init__(self, name):
        self.name=name
class Child(Parent):
    def __init__(self,name, age):
        super().__init__(name)
        self.age=age
    def show(self):
        print(self.name, self.age)
a=Child("raju", 33)
a.show()

print("*************************")
class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def show(self):
        print(self.name, self.salary)


e = Employee("Ravi", 50000)
e.show()
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
class A:
    def __new__(cls):
        return super(A,cls).__new__(cls)
        return super(A,cls).__new__(cls)
        
    
    def __init__(self):
        print("instance is created")
a=A()

