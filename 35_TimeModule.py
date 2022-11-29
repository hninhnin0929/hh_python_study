import time;

def myFun(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    avgTime = (end - start)/rep
    fn(avgTime)

myFun(print, 1, 2, 3, sep="-", end="***\n",rep=5)
