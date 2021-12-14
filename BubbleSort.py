# Python program to demonstarte bubble sort

class BubbleSorting():

    #function to printArray
    def printArray(self, arr, lengthOfArray):
        print("The elements of the array before sorting: ", end=" ")
        for i in range(lengthOfArray):
            print(arr[i], end=" ")

    # function containing bubble sort logic
    def logicBubbleSort(self, arr, lengthOfArray):
        # loop for the number of passes
        for i in range(lengthOfArray-1):
            for j in range(lengthOfArray-1-i):
                if(arr[j]>arr[j+1]):
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp

    
     # function containing bubble sort logic
    def logicBubbleSortAdaptive(self, arr, lengthOfArray):
        isSorted = False
        passCount = 0
        # loop for the number of passes
        for i in range(lengthOfArray-1):
            isSorted = True
            for j in range(lengthOfArray-1-i):
                if(arr[j]>arr[j+1]):
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
                    isSorted = False
            
            if(isSorted):
                break
            passCount = passCount +1
        
        #print number of number of pass
        print("The number of passes taken :", end=" ")
        print(passCount)




# driver code 

# Taking array inout from the user 
print("Please enter the elements of the array separted by a space and hit enter when done: ")
myArr = list(map(int, input().split()))

#length of the array
n = len(myArr)

#creating object the of the class
obj = BubbleSorting()

#calling the member functions
obj.printArray(myArr, n)
obj.logicBubbleSortAdaptive(myArr, n)
obj.printArray(myArr, n)

