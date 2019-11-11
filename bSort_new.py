import time
import random
# Help function to find the place for the insert sort function.



def findPlace(array, value, start, end):

    # Base the fist time it just add the number.
    if start == end:
        if array[start] > value:
            return start
        else:
            return start+1


    # Return start position if we wen to far.
    if start > end:
        return start

    
    # By converting to an it it becomes Floor.
    mid = int((start+end)/2)


    # If it is is bigger make a new jump
    if array[mid] < value:
        return findPlace(array, value, mid+1, end)

    # If it is more then make a new jummp.
    elif array[mid] > value:
        return findPlace(array, value, start, mid-1)

    # If it is exat you can place it there.
    else:
        return mid



# Function takes a list of Ints and returns it Sorted.
def bSort(array):

    for i in range(1,len(array)):
        
        # Pick out the value first.
        value = array[i]
        
        # Find the place is handeld by the Binary search called findPlace
        insertIndex = findPlace(array, value, 0 , i-1)
        
        #Place the nummber in the right position.
        array = array[:insertIndex] + [value] + array[insertIndex:i] + array[i+1:]

    return array


def randomlist(n):
    array = []

    for n in range(0,n):
        array.append(random.randint(0,10000))

    return array



# Short array list with some ints.
array = [5,2,3,6,7,8,10,11,9,12,18,19,5677]
array = randomlist(10000)
ts = time.time()
bSort(array)
ts = (time.time() - ts)
print ("It took " + str(ts) + " sec to complete")
print("\n\n\n")





