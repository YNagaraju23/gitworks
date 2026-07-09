class dec_function:
    def my_decorator(func):
        def wrapper(c,d):
            result = c+d
            #result=func(c,d)
            return result
        return wrapper
    @my_decorator
    def mul(a,b):
        return a*b
    print(mul(2,3))
    #########################################

    def decorator_function(func):
        def print_mul(a):
            return a*30
        return print_mul
    @decorator_function
    def print_mul(a):
        return a*10

    print(print_mul(5))

    ####################################################
    def dec_function(func):
        def wrapper():
            result=func().upper()
            return result
        return wrapper
    @dec_function
    def say_hello():
        return "hello world"
    print(say_hello())
    #################################################
    def dec_function(func):
        def wrapper():
            result=func().upper()
            return result
        return wrapper
    @dec_function
    def say_hello():
        return "hello world"
    print(say_hello())