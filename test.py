from timeit import default_timer as timer
import statistics

def meaure():
    sizes = [10, 100, 1000, 10000]

    nr = []
    sqn = []
    phn = []

    for s in sizes:
        print(s)
        for br in range(0, s):
            arr = genArr(s, br);
            time(n_search, arr, nr)
            time(nsqr_search, arr, sqn)
            time(pshalf_search, arr, phn)

    print('n', statistics.mean(nr))
    print('sn', statistics.mean(sqn))
    print('pn', statistics.mean(phn))

def time(alg, arr, res):
    now = timer()
    alg(arr)
    now2 = timer()
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

    p = -1;
    lp = -1;
    for i in range(0, s, jump):
        if arr[i] == 0:
            lp = p
            p = i
        elif arr[i] == 1: 
            break

    for i in range(lp, p):
        if arr[i] == 0: return i

    return -1


def pshalf_search(arr):
    return -1



meaure()