from timeit import default_timer as timer
import statistics
import math

def meaure():
    sizes = [100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]

    for s in sizes:
        nr = []
        sqn = []
        phn = []
        print(s)
        progress = 0
        for br in range(1, s, int(s/100)): # ~100 cases/points
            # if 100*float(br)/s >= progress + 1: 
            #     progress += 1
                # print(str(progress) + '%')
            arr = genArr(s, br);
            time(n_search, arr, nr, br)
            time(pshalf_search, arr, phn, br)
            time(nsqr_search, arr, sqn, br)
        
        print('n', statistics.mean(nr))
        print('phn', statistics.mean(phn))
        print('sqn', statistics.mean(sqn))


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

    p = 0
    f = False
    for i in range(0, s, jump):
        p = i
        if arr[i] == 1:
            f = True 
            break

    if f:
        for i in range(p-jump, p+1):
            if arr[i] == 1: 
                return i
    else:
        for i in range(p, s):
            if arr[i] == 1: 
                return i
    return -1


def pshalf_help(arr, lo, hi):
    m = math.floor(lo + (hi - lo) / 2)

    if arr[m] == 0:
        return pshalf_help(arr, m, hi)
    
    for i in range(lo, hi):
        if arr[i] == 1: return i


    return -1

def pshalf_search(arr):
    return pshalf_help(arr, 0, len(arr))

meaure()