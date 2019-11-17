import time
import random
import math
import timeit


# skappar en osoterad lista.
def randomList(n):

    return [random.randint(1,10000) for _ in range(n)]



# Skappar en Soterad Lista
def sortedList(n):
    sortedlist = []
    for x in range(1, n+1, 1):
        sortedlist.append(x)

    return sortedlist



# Skappar en nästan soterad lista.
def almostSorted(n):
    alSort = []
    for x in range(1, n+1, 1):
        alSort.append(x)
    return alSort


#Inplace Insertion_Sort
def insertion_sort(numlist):

    for index in range(1,len(numlist)):

        currentvalue = numlist[index]
        position = index

        while position>0 and numlist[position-1]>currentvalue:
            numlist[position]=numlist[position-1]
            position = position-1

        numlist[position]=currentvalue

    return numlist


def insertion_sort_binary(numlist):

    for index in range(1, len(numlist)):

        currentvalue = numlist[index]
        bottom, top = 0, index

        while bottom < top:
            middle = (bottom + top) // 2
            if numlist[middle] < currentvalue:
                bottom = middle + 1
            else:
                top = middle

        numlist[:] = numlist[:bottom] + [currentvalue] + numlist[bottom:index] + numlist[index + 1:]
    return numlist


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
        return insertion_sort_binary(l)

    al = binMergeSort(l[:lenght // 2  +1], k)
    bl = binMergeSort(l[lenght // 2  +1:], k)

    return merge(al, bl)

def insMergeSort(l, k):
    lenght = len(l)
    if lenght <= k:
        return insertion_sort(l)
    
    al = insMergeSort(l[:lenght // 2  +1], k)
    bl = insMergeSort(l[lenght // 2  +1:], k)

    return merge(al, bl)



def merge_sort(numlist):

    if(len(numlist) > 1):

        middle = len(numlist) // 2
        lefthalf, righthalf = numlist[:middle], numlist[middle:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i, j, k = 0, 0, 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                numlist[k]=lefthalf[i]
                i=i+1
            else:
                numlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            numlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            numlist[k]=righthalf[j]
            j=j+1
            k=k+1
    
    return numlist


# Kör testerna av algoritmerna.
x = 4096

#print("binMergesort timing:")
for i in range(1, 7, 1):
    a = sortedList(x)

    timestp = time.time()
    binMergeSort(a,64)
    print(str(x) + "    " + str(time.time()-timestp) + "   Merge Binary")

    timestp = time.time()
    insMergeSort(a,64)
    print(str(x) + "    " + str(time.time()-timestp) + "   Merge Insert")

    timestp = time.time()
    merge_sort(a)
    print(str(x) + "    " + str(time.time()-timestp) + "   Merge ")

    x = x*2

#print("insMergeSort timing:")
#for i in range(1, 7, 1):
#    time = timeit.timeit('a = insMergeSort(a, 2)', globals=globals(), setup="a = sortedList(x)", number=5) 
#    print(str(x) + "    " + str(time))
#    x = x*2

