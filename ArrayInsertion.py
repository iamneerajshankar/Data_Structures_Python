"""
* A Java program to show insertion of element in an already existing array
* An element can be inserted in an array at a specific position. For this operation to succeed,
* the array must have enough capacity.
"""


class ArrayInsertion:

    # method to print array
    def print_array(self, n, arr):

        for i in range(0, n):
            print(arr[i], end=" ")
        print()

    # array insertion logic takes four arguments, size(n), arr, index, element(to be inserted)
    def insert_at_index(self, n, arr, index, element):

        arr.insert(index, element)


# driver code

if __name__ == "__main__":

    print("Please enter the array elements separated by space: ")
    arr = list(map(int, input().split()))

    n = len(arr)
   # total_size = n +1

    print("Please enter the index where element to be inserted: ", end=" ")
    index = int(input())

    print("Please enter the element to be inserted: ", end=" ")
    element = int(input())

    # create the ArrayInsertion class instance
    arrayInsertion = ArrayInsertion()

    print("The elements of the before insertion: ", end=" ")
    arrayInsertion.print_array(n, arr)

    arrayInsertion.insert_at_index(n, arr, index, element)
    print("The elements of the array after insertion: ", end=" ")
    n = n+1
    arrayInsertion.print_array(n, arr)
