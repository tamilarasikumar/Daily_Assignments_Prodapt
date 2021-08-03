import timeit

# def printnumbers():
#     for i in range(1000):
#         pass
# def printwhile():
#     n=0
#     while(n<=1000):
#         n=n+1
#         pass
# print(timeit.timeit(printnumbers,number=10000000))
# print(timeit.timeit(printwhile,number=10000000))
list = [1,2,4,55,64,66,82,992]
def f1():
    filter(46,list)
def f2():
    for i in list:
        if (i==46):
            pass
print(timeit.timeit(f1))
print(timeit.timeit(f2))