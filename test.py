def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def sum_print():
    a = 5
    b = 10
    print(a + b)

sum_print()


    