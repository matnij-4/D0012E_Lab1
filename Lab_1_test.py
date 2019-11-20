import time
import random
import math
import timeit


# skappar en osoterad lista.
def randomList(n):
    randomlist = []
    for x in range(1, n+1, 1):
        randomlist.append(random.randint(1,10000))
        
    return randomlist


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



# Skappar en lista med allt fel.
def worstList(n):
    worstSorted = []
    for x in range(n, 0, -1):
        worstSorted.append(x)
    return worstSorted


        


#Inplace Insertion_Sort
def insertion_sort(numlist):

    #Går igenom listan n gånger
    for index in range(1,len(numlist)):
        
        #Laddar inte värdet för att gemföra.
        currentvalue = numlist[index]
        position = index

        # Hitta platsen för den värde. (SWAP) Sen lopa igenom listan så allt är på rätt plats.
        while position>0 and numlist[position-1]>currentvalue:
            numlist[position]=numlist[position-1]
            position = position-1

        numlist[position]=currentvalue

    return numlist


# bSort
def insertion_sort_binary(numlist):

    #Går igenom listan n gånger
    for index in range(1, len(numlist)):

        #Laddar inte värdet för att gemföra.
        currentvalue = numlist[index]
        bottom, top = 0, index

        # Hittar platsen för värdet.
        while bottom < top:
            #Delar listan på 2.
            middle = (bottom + top) // 2

            #Kollar om värdet är övber eller under.
            if numlist[middle] < currentvalue:
                bottom = middle + 1
            else:
                top = middle

                
        #Flyttar listan och siffran till rätt plats.
        for i in range(index, bottom, -1):
            numlist[i] = numlist[i - 1]

        numlist[bottom] = currentvalue
        
    return numlist


#Merge Sort med Insert lånad av GeekforGeeks och sedan Omsrkiven till att dela med k
def merge_sort_insert(numlist, k):

    #Delar upp listan tills den är rätt Storlek.
    if len(numlist)>k:

        #Delar på mitten.
        middle = len(numlist) // 2
        lefthalf, righthalf = numlist[:middle], numlist[middle:]

        merge_sort_insert(lefthalf, k)
        merge_sort_insert(righthalf, k)


        #Pekare på var i listan
        i, j, t = 0, 0, 0


        # Merge alla sublistor.
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                numlist[t]=lefthalf[i]
                i=i+1
            else:
                numlist[t]=righthalf[j]
                j=j+1
            t=t+1

        while i < len(lefthalf):
            numlist[k]=lefthalf[i]
            i=i+1
            t=t+1

        while j < len(righthalf):
            numlist[k]=righthalf[j]
            j=j+1
            t=t+1
    #När den är rätt storlekt så soterar man sub listorna.
    else:
        insertion_sort(numlist)

    return numlist



#Merge Sort med Binär lånad av GeekforGeeks och sedan Omsrkiven till att dela med k
def merge_sort_binary(numlist, k):

    #Delar upp listan tills den är rätt Storlek.
    if len(numlist)>k:

        middle = len(numlist) // 2
        lefthalf, righthalf = numlist[:middle], numlist[middle:]

        #Recusived deling av listan
        merge_sort_binary(lefthalf, k)
        merge_sort_binary(righthalf, k)


        #Pekare på var i listan
        i, j, t = 0, 0, 0

        #Merge alla sublistor.
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                numlist[t]=lefthalf[i]
                i=i+1
            else:
                numlist[t]=righthalf[j]
                j=j+1
            t=t+1

        #Om listan är slut fyll bara på den andra.
        while i < len(lefthalf):
            numlist[t]=lefthalf[i]
            i=i+1
            t=t+1

        while j < len(righthalf):
            numlist[t]=righthalf[j]
            j=j+1
            t=t+1
            
    #När den är rätt storlekt så soterar man sub listorna.
    else:
        insertion_sort_binary(numlist)

    return numlist



#Merge Sort lånad av Geeks for Geeks och om skriven lite.
def merge_sort(numlist):

    # Delar listan i hälften tills bara ett elemnt i listan
    if(len(numlist) > 1):

        middle = len(numlist) // 2
        lefthalf, righthalf = numlist[:middle], numlist[middle:]

        #Recusived deling av listan
        merge_sort(lefthalf)
        merge_sort(righthalf)


        #Pekare på var i listan
        i, j, k = 0, 0, 0

        
        # Merge allt till listorna.
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                numlist[k]=lefthalf[i]
                i=i+1
            else:
                numlist[k]=righthalf[j]
                j=j+1
            k=k+1


        #Om listan är slut fyll bara på den andra.
        while i < len(lefthalf):
            numlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            numlist[k]=righthalf[j]
            j=j+1
            k=k+1
    
    return numlist




# Testar listor
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
    a = sortedList(x)
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

