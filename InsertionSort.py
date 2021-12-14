# python program to deomonstrate insertion sort 
class InsertionSorting:

    #print function to print the elements of the array

    def printArray(self, arr, lengthOfArray):
        print("The elements of the array are: ", end=" ")
        for i in range(lengthOfArray):
            print(arr[i], end=" ")
        print()

    # function containing the logic of the inserstion sort
    def InsertionSorting(self, arr, lengthOfArray):
        for i in range(1, lengthOfArray):
            key = arr[i]
            j = i-1

            while(j>=0 and arr[j]>key):
                arr[j+1]=arr[j]
                j = j-1
            
            arr[j+1] = key


# driver code

print("Please enter the elements of the array separated by a space and hit enter once done", end="\n")
myArr = list(map(int, input().split()))
n = len(myArr)

#creating the object the given class
obj = InsertionSorting()

#calling the member functions 
obj.printArray(myArr, n)
obj.InsertionSorting(myArr, n)
obj.printArray(myArr, n)