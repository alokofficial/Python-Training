import time
def fib(n,d):
    if n in d:
        return d[n]
    else:
        value=fib(n-1,d)+fib(n-2,d)
        d[n]=value
        return value
start=time.time()
d={0:1,1:1}
print(fib(996,d),time.time()-start,"secs")
