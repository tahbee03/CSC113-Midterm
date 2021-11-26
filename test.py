# BASED ON MATERIAL FOUND FROM: https://www.geeksforgeeks.org/get-current-timestamp-using-python/
import datetime


def foo():
    dt = datetime.datetime.now()
    print("Function foo() called! [Timestamp: " + str(dt) + "]")


foo()
print("junk")
foo()
foo()
a = input("Enter something: ")
print(a)
foo()



