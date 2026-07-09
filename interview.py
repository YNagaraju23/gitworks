dict1={

  'Input.txt': 'Sri',

  'Code.py': 'lakshmi',

  'Output.txt': 'Sri'

}

list1=list(dict1.values())
print(list1)
seen = []
duplicate =[]
for i in list1:
    seen.append(i)
else:
    duplicate.append(i)
print(seen)
print(duplicate)
for i in duplicate:
    

#expected output {

#  “Sri”: ['Input.txt', 'Output.txt'],

#  “Lakshmi”: ['Code.py']

#}
 ***********************************************
 import re
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
list1=[]
for i in words:
    i.split()
    list1.append(i.sorted())
print(list1)
    

#output :
#[
# ["eat", "tea", "ate"],
# ["tan", "nat"],
# ["bat"]
#]