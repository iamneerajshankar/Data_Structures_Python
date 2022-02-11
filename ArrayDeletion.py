"""
* A python program for deletion of an element from an arr
* An element at a specified position can be deleted, creating a void that needs
* to be fixed by shifting all the elements to their adjacent left
"""


class ArrayDeletion:

    # method to traverse and print array element
    def print_array(self, n, arr):

        for i in range(0, n):
            print(arr[i], end=" ")
        print()

    # method to delete an element using while loop
    def del_from_index(self, n, arr, index):
        i = index
        while(i < n-1):
            arr[i] = arr[i+1]
            i = i+1

    # method to delete an element using for loop
    def del_using_for(self, n, arr, index):
        for i in range(index, n-1):
            arr[i] = arr[i+1]


# driver code
if __name__ == "__main__":

    print("Please enter the array elements separated by a space: ")
    arr = list(map(int, input().split()))
    n = len(arr)

    print("Please enter the index from element to be deleted: ", end=" ")
    index = int(input())

    # create the ArrayDeletion class instance
    arrayDeletion = ArrayDeletion()

    print("The elements of the before insertion: ", end=" ")
    arrayDeletion.print_array(n, arr)

   # arrayDeletion.del_from_index(n, arr, index)
    arrayDeletion.del_using_for(n, arr, index)
    print("The elements of the array after insertion: ", end=" ")
    n = n-1
    arrayDeletion.print_array(n, arr)
