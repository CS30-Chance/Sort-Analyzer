# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
# print(randomData[0:50])
# print(reversedData[0:50])
# print(nearlySortedData[0:50])
# print(fewUniqueData[0:50])


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")

def bubbleSort(anArray):
    length = len(anArray)
    for compares in range(1, length):
        for position in range(length - compares):
            if anArray[position] > anArray[position + 1]:
                anArray[position + 1], anArray[position] = anArray[position], anArray[position + 1]
    return anArray


def selectionSort(anArray):
    length = len(anArray)
    for fillSlot in range(length - 1):
        minimum = anArray[fillSlot]
        min_index = fillSlot
        for Number_after in range(fillSlot, length):
            if minimum > anArray[Number_after]:
                minimum = anArray[Number_after]
                min_index = Number_after
        anArray[fillSlot], anArray[min_index] = anArray[min_index], anArray[fillSlot]
    return anArray


def insertionSort(anArray):
    length = len(anArray)
    for i in range(1, length):
        value = anArray[i]
        position = i
        while position > 0 and anArray[position - 1] > value:
            position -= 1
        anArray.pop(i)
        anArray.insert(position, value)
    return anArray


data = [randomData, reversedData, nearlySortedData, fewUniqueData]
names = ['randomData', 'reversedData', 'nearlySortedData', 'fewUniqueData']
for d in range(4):
    startTime = time.time()
    bubbleSort(data[d])
    endTime = time.time()
    print(f"Bubble Sort {names[d]}: {endTime - startTime} seconds")

for d in range(4):
    startTime = time.time()
    selectionSort(data[d])
    endTime = time.time()
    print(f"Selection Sort {names[d]}: {endTime - startTime} seconds")

for d in range(4):
    startTime = time.time()
    insertionSort(data[d])
    endTime = time.time()
    print(f"Insertion Sort {names[d]}: {endTime - startTime} seconds")



