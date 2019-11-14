import time
import random
import math


# skappar en osoterad lista.
def randomList(n):

    return [random.randint(1,10000) for _ in range(n)]



# Skappar en Soterad Lista
def sortedList(n):
    sortedlist = []
    for x in range(1, 10000, 1):
        sortedlist.append(x)

    return sortedlist



# Skappar en nästan soterad lista.
def almostSorted(n):
    alSort = []
    for x in range(1, 10000, 1):
        alSort.append(x)
    return alSort



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



