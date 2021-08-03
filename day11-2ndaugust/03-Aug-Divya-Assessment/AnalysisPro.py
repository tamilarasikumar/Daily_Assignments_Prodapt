import timeit
#print(timeit.timeit(stmt="a=10;b=5; c=a+b"))
print(timeit.timeit(stmt="z=50*5"))
mycode  = '''
a =10; 
if (a<15):
    pass '''
print(timeit.timeit(stmt=mycode))