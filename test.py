from timeit import default_timer as timer
import statistics
import math

def meaure():
    sizes = [10, 100, 1000, 10000]

    nr = []
    sqn = []
    phn = []

    for s in sizes:
        print(s)
        for br in range(1, s):
            arr = genArr(s, br);
            time(n_search, arr, nr, br)
            time(nsqr_search, arr, sqn, br)
            time(pshalf_search, arr, phn, br)

    print('n', statistics.mean(nr))
    print('sn', statistics.mean(sqn))
    print('pn', statistics.mean(phn))

def time(alg, arr, res, expected):
    now = timer()
    answer = alg(arr)
    now2 = timer()

    if (answer != expected): raise Exception('failed', answer, expected) 
    res += [now2-now]

def genArr(size, break_point):
    arr = [0 for i in range(0, size)]
    for i in range(break_point, size):
        arr[i] = 1;
    return arr

def n_search(arr):
    for i in range(0, len(arr)):
        if arr[i] == 1:
            return i;
    return -1

def nsqr_search(arr):
    s = len(arr)
    jump = math.floor(math.sqrt(s));

    p = 0;
    for i in range(0, s, jump):
        p = i
        print('i', i)
        if arr[i] == 1: 
            break

    for i in range(p-jump, p+1):
        print('ii', i, p)
        if arr[i] == 1: 
            print('res', i)
            return i

    return -1


def pshalf_help(arr, lo, hi):
    m = math.floor(lo + (hi - lo) / 2)

    if arr[m] == 0:
        return pshalf_search(arr, m, hi)
    
    for i in range(lo, hi):
        if arr[i] == 1: return i


    return -1

def pshalf_search(arr):
    return pshalf_help(arr, 0, len(arr))

meaure()