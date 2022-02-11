"""
* A java program to demonstrate the bubble sort algorithm - With bubble sort,
* we intend to ensure that the largest element of the segment reaches the last
* position at each iteration.
* Time Complexity of the bubble sort algorithm is O(n2).
* It is a stable algorithm, because it preserves the order of equal elements.
* It is not a recursive algorithm.
* Bubble sort is not adaptive by default, but can be made adaptive by modifying the program.

"""


class BubbleSortAlgorithm:

    # method to traverse and print array element
    def print_array(self, n, arr):

        for i in range(0, n):
            print(arr[i], end=" ")
        print()

    def bubble_sort_logic(self, n, arr):

        for i in range(0, n):  # outer loop for number iterating each element

            for j in range(0, n-1-i):  # inner loop for the number of passes
                if(arr[j] > arr[j+1]):
                    temp = arr[j+1]
                    arr[j+1] = arr[j]
                    arr[j] = temp

    def bubble_sort_adaptive(self, n, arr):

        no_of_passes = 0
        isSorted = False

        for i in range(0, n):  # outer loop for number iterating each element
            no_of_passes = no_of_passes + 1
            isSorted = True  # we assume array is sorted at each iteration
            for j in range(0, n-1-i):  # inner loop for the number of passes

                if(arr[j] > arr[j+1]):
                    isSorted = False  # when the enters the if statement, it means array is not sorted
                    temp = arr[j+1]
                    arr[j+1] = arr[j]
                    arr[j] = temp

            if(isSorted):
                print("The number of passes taken {}".format(no_of_passes))
                return


# driver code
if __name__ == "__main__":

    print("Please enter the array elements separated by space", end="\n")
    arr = list(map(int, input().split()))
    n = len(arr)

    # create BubbleSortAlgorithm class instance
    sorting = BubbleSortAlgorithm()

    print("The array elements before sorting: ", end=" ")
    sorting.print_array(n, arr)

    sorting.bubble_sort_adaptive(n, arr)
    print("The array elements after sorting: ", end=" ")
    sorting.print_array(n, arr)
