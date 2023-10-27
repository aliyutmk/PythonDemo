from threading import Thread
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(50):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(50):
            print("Hi")
            sleep(1)

hello = Hello()
hi = Hi()

hello.start()
sleep(0.2)
hi.start()
hello.join()
hi.join()
print("This is the end")