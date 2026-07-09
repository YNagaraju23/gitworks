import matplotlib.pyplot as plt
def plot_test():
    f=open('age_data.txt','r')
    age_data = f.readlines()
    age_list=[]
    for i in age_data:
        print(i)
        age_list.append(int(i))
    print(age_list)
print("Age data from the file:")
plot_test()