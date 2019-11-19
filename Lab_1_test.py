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
    flag = True
    for x in range(1, n+1, 1):
        if flag:
            alSort.append(x-1)
            
            flag = False
        else:
            alSort.append(x+1)
            flag = True
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


#        numlist[:] = numlist[:bottom] + [currentvalue] + numlist[bottom:index] + numlist[index + 1:]

        for i in range(index, bottom, -1):
            numlist[i] = numlist[i - 1]

        numlist[bottom] = currentvalue
        
    return numlist


def merge_sort_insert(numlist, minlength):


    if len(numlist)>minlength:

        middle = len(numlist) // 2
        lefthalf, righthalf = numlist[:middle], numlist[middle:]

        merge_sort_insert(lefthalf, minlength)
        merge_sort_insert(righthalf, minlength)

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
    else:
        insertion_sort(numlist)

    return numlist




def merge_sort_binary(numlist, minlength):

    if len(numlist)>minlength:

        middle = len(numlist) // 2
        lefthalf, righthalf = numlist[:middle], numlist[middle:]

        merge_sort_binary(lefthalf, minlength)
        merge_sort_binary(righthalf, minlength)

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
    else:
        insertion_sort_binary(numlist)

    return numlist



#Merge Sort
def merge_sort(numlist):

    # Delar listan i hälften tills bara ett elemnt i listan
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


def isSorted(a):
    last = a[0]
    for x in a[1:]:
        if x < last:
            return False
        last = x

    return True

# Kör testerna av algoritmerna.
x = 4096

#print("binMergesort timing:")
for i in range(1, 11, 1):
    a = randomList(x)
    b = a.copy()
    c = a.copy()

    timestp = time.time()
    merge_sort_binary(a,32)
    print(str(x) + "    " + str(time.time()-timestp) + "   Merge Binary")

    timestp = time.time()
    merge_sort_insert(b,32)
    print(str(x) + "    " + str(time.time()-timestp) + "   Merge Insert")

    timestp = time.time()
    merge_sort(c)
    print(str(x) + "    " + str(time.time()-timestp) + "   Merge ")

    x = x*2

#print("insMergeSort timing:")
#for i in range(1, 7, 1):
#    time = timeit.timeit('a = insMergeSort(a, 2)', globals=globals(), setup="a = sortedList(x)", number=5) 
#    print(str(x) + "    " + str(time))
#    x = x*2

