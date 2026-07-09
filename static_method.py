#static method
# A static method is a method that belongs to a class rather than an instance of the class. It can be called on the class itself, without needing to create an instance. Static methods are defined using the @staticmethod decorator and do not have access to the instance (self) or class (cls) variables. They are typically used for utility functions that perform a task related to the class but do not require access to instance or class data.
class MyClass:
    @staticmethod
    def my_static_method():
        print("This is a static method.")