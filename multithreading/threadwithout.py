from threading import *
import time

class MyClass:
    def job(self):
        time.sleep(2)
        print("child")
ob=MyClass()
t=Thread(target=ob.job())
t.start()
for i in range(3):
    print("main",i)