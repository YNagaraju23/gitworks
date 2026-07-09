#monkey patching
"""monkey patching is a technique in programming where you can modify or extend the behavior of libraries or classes at runtime without changing their source code. This can be useful for fixing bugs, adding features, or altering behavior in a way that is not possible through inheritance or composition. However, it should be used with caution as it can lead to unexpected side effects and make code harder to maintain."""
class A:
    def greet(self):
        return "Hello, World!"
def new_greet(self):
    return "Hi there!"

A.greet = new_greet
OBJ = A()
print(OBJ.greet())