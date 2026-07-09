#Closures in Python are like “memory-equipped” functions. They allow a function to remember values from the environment in which it was created even if that environment no longer exists. Closures are used in functional programming, event handling and callback functions where you need to retain some state without using global variables.
def outer_function(x):
    def inner_function(y):
        return x+y
    return inner_function
    
sum=outer_function(20)
print(sum(10))

print("******************************")

def outer_function(a):
    def inner_function(x):
        def internal_inner(y):
            return x+y+a
        return internal_inner
    return inner_function
result=outer_function(20)
result_1=result(30)
print(result_1(40))

def outer_function(a):
    def inner_function(b):
        return a+b
    return inner_function
inner_function_result=outer_function(20)
b=inner_function_result(10)
print(b)


def outer_function(a):
    def inner_function(b):
        return a+b
    return inner_function
a=outer_function(5)
print(a)
b=a(6)
print(b)