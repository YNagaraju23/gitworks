#second heighest integer in list
list1=[10,20,30,40]
number = 0
for i in list1:
    if i > number:
        number = i
print(number)
sec_high = 0
for i in list1:
    if i>sec_high and number>i:
        sec_high = i
print("second highest is", sec_high)