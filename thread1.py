import threading
import time
def print_text(name):
    print(f'{name}')
t1=threading.Thread(target=print_text, args=("raju",))
t1.start()
#t1.join()
print("done!")


def print_sum(a,b):
    print(a+b)

t1=threading.Thread(target=print_sum,args=(20,40))
time.sleep(2)
t2=threading.Thread(target=print_sum,args=(67,40))
t1.start()
t2.start()
