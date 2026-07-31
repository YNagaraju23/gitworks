#class User:
#    def __init__(self):
#        self.name = "Alice"
#        self.email = "alice@example.com"
#
#user = User()
#fields = ["name", "email"]
#
#for field in fields:
    # Dynamically prints "Alice", then "alice@example.com"
#    print(getattr(user, field))

print("******************************************************")





class Friend:
    def __init__(self):
        self.name="Nagaraju"
        self.age=25
friend=Friend()
fields=["name","age"]


for field in fields:
    print(getattr(friend,field))#getattr(object,parameter list)



print("**********************************************")

class Fruit:
    def __init__(self):
        self.value="5"

object_1=Fruit()
#lst=["value"]
#for list_item in lst:

print(getattr(object_1, "value"))
