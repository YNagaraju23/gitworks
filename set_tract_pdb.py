
def my_decorator(func):
    def wrapper():
        result=func().upper()
        return result
    return wrapper


@my_decorator
def print_hello():
    return "hello world"
print(print_hello())



def my_decorator(func):
    def wrapper(a,b):
        return a*b
    return wrapper
@my_decorator
def print_mul(x,y):
    return x+y
print(print_mul(28,48))
        

