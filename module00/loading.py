
# iterables: types of data on which it is possible to iterate (list, str, file...) with for .. in 
#   methods:
#       - __iter__()  that returns an iterator
#       - Or at least __getitem__()
# ------------------------------------------------------------------------------------------------
# iterators: special kind of iterable which can only be read once with the help of next() 
#   methods:
#       - __iter__() that returns self
#       - __next__() that returns next value (StopIteration when done)
#       
# iterator = iter(iterable) (calls iterable.__iter__())
# print(next(iterator)) => print first value
# print(next(iterator)) => print second value...
#
# for loops implicitly calls iter() and next()
# ------------------------------------------------------------------------------------------------
# generators: iterators that generate the values on the fly / do not store in memory.
# It leads to better performance. 
#
# generator = (x*x for x in range(3))
# ------------------------------------------------------------------------------------------------ 
# yield: keyword that makes a function become a generator
# def my_generator():
# ...
# yield 1
# ...
# yield 2
#
# gen = my_generator()
# value = next(gen)
# => at first call, nothing runs. Then at each call, the function 'pauses' at each yield
# using it in a for loop is the same as calling next() multiple times
from time import time
from time import sleep

def ft_progress(lst):
    size = len(lst)
    progress_bar = ""
    print()
    start = time()
    for i in lst:
        progress_bar = (i * 22 // size) * "="   # 22 cases
        space = (21 - (i * 22 // size)) * " " 
        end = time()
        if i == 0:
            estimated_time = 0
        else:
            estimated_time = ((end - start) * size) / i
        print(f"\033[F ETA: {round(estimated_time, 2):.2f}s [{(i/10):02.0f}%][{progress_bar}>{space}] {i}/{size}" # \033[F  -> clear terminal
            f"| elapsed time {round(end - start, 2)}s")
        yield i # se souvient ou il s'etait arrete
        

# main
try:
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        # ft_progress is a generator
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)
except BaseException:
    print("stop")
