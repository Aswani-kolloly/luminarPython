#multi tasking
#1) multi processing
#2) multi threading
#fast context switching takes place
import threading
import time

def disp():
    for i in range(1,3):
        #time.sleep(3)
        print(threading.currentThread().getName())
t=threading.Thread(target=disp)
t.start()
for i in range(1, 3):
    print(threading.currentThread().getName())