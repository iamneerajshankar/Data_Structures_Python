"""
* A python program to demonstrate basic understanding of array. 
* Array in Python can be created by importing array module. array(data_type, value_list)
  is used to create an array with data type and value list specified in its arguments. 
* However, we will implement array operation in data structures using list for the convenience.
* array is a collection of items stored at contiguous memory locations. The idea
  is to store multiple items of the same type together.

"""

from ast import comprehension


class UnderstandingTheArray:

    # method to traverse and print array element
    def print_array(self, n, arr):

        for i in range(0, n):
            print(arr[i], end=" ")
        print()

    # multiple ways to traverse a list in reverse order
    def with_while_loop(self, n, arr):
        i = n-1
        while i >= 0:
            print(arr[i], end=" ")
            i = i - 1
        print()

    def using_for_loop(self, n, arr):
        for i in range(n-1, -1, -1):
            print(arr[i], end=" ")
        print()

    def using_reversed_function(self, n, arr):
        # reversed() function returns an iterator to accesses the given list in the reverse order.
        for i in reversed(arr):
            print(arr[i], end=" ")
        print()

    def with_list_comprehension(self, n, arr):
        # Iterate over the list using List Comprehension and [::-1]
        [print(i, end=" ") for i in arr[::-1]]


# driver code
if __name__ == "__main__":

    print("Please enter the elements of your array separated by a space", end="\n")
    arr = list(map(int, input().split()))
    n = len(arr)

    # create UnderstandingTheArray class instance
    understandingTheArray = UnderstandingTheArray()

    # calling the member functions
    print("The elements of the array: ", end=" ")
    understandingTheArray.print_array(n, arr)

    print("The elements of the array in reverse order using while loop: ", end=" ")
    understandingTheArray.with_while_loop(n, arr)

    print("The elements of the array in reverse order using for loop: ", end=" ")
    understandingTheArray.using_for_loop(n, arr)

    print("The elements of the array in reverse order using reversed function: ", end=" ")
    understandingTheArray.using_for_loop(n, arr)

    print("The elements of the array in reverse order using list comprehension : ", end=" ")
    understandingTheArray.using_for_loop(n, arr)
