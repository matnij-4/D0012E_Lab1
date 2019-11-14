# bSort an insertyionsort with binary search
import random
import timeit


def bin_search(a, x, high):
    low = 0

    while True:
        if low == high:
            if a[low] < x:
                return low + 1
            else:
                return low

        if low > high:
            return low

        mid = (high + low) // 2

        if x < a[mid]:
            high = mid - 1
        elif x > a[mid]:
            low = mid + 1
        else:
            return mid

        
def insertsort(a):
    for i in range(1, len(a)):
        x = a[i]
        for n in range(0, i):
            if a[n] > x:
                a = a[:n] + [x] + a[n:i] + a[i+1:]

    return a


def bSort(ilist):
    
    for i in range(1, len(ilist)):
        x = ilist[i]
        pos = bin_search(ilist, x, i - 1)
        ilist = ilist[:pos] + [x] + ilist[pos:i] + ilist[i+1:]

    return ilist


def merge(al, bl):
    cl = []
    while len(al) > 0 and len(bl) > 0:
        if al[0] < bl[0]:
            cl.append(al[0])
            al = al[1:]
        else:
            cl.append(bl[0])
            bl = bl[1:]

    if len(bl) > 0:
        cl += bl
    else:
        cl += al

    return cl

def binMergeSort(l, k):
    lenght = len(l)
    if lenght <= k:
        return bSort(l)

    al = binMergeSort(l[:lenght // 2  +1], k)
    bl = binMergeSort(l[lenght // 2  +1:], k)

    return merge(al, bl)

def insMergeSort(l, k):
    lenght = len(l)
    if lenght <= k:
        return insertsort(l)
    
    al = binMergeSort(l[:lenght // 2  +1], k)
    bl = binMergeSort(l[lenght // 2  +1:], k)

    return merge(al, bl)

def isSorted(a):
    last = a[0]
    for x in a[1:]:
        if x < last:
            return False
        last = x

    return True
    
    
        
# testcode
flag = True
random.seed()

def rndlist(n):
    a = []
    for n in range(0, n):
        a.append(random.randint(0, 10000))
    return a

def sortlist(n):
    a = []
    for n in range(0,n):
        a.append(n)
    return a

bestTime = 200

print("binMergesort timing:")
for x in range(50, 2000, 50):
    time = timeit.timeit('a = binMergeSort(a, x)', globals=globals(), setup="a = rndlist(30000)", number=5) 
    print(str(x) + "    " + str(time))
    if ( bestTime > time):
        bestTime = time
        print(time)

print( "This might be the best K " + str(bestTime))

bestTime = 200

print("insMergeSort timing:")
for x in range(50, 2000, 50):
    time = timeit.timeit('a = insMergeSort(a, x)', globals=globals(), setup="a = rndlist(30000)", number=5) 
    print(str(x) + "    " + str(time))
    if ( bestTime > time):
        bestTime = time
        print(time)

print( "This might be the best K " + str(bestTime))

