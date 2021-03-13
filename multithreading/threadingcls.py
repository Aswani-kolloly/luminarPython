from threading import *
class MyThread(Thread):
    def run(self):
        for i in range(3):
            print("child thread",i)
ob=MyThread()
ob.start()
for i in range(3):
    print("main thread",i)
