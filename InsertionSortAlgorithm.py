"""
* A python program to demonstrate Insertion sort. In Insertion sort, we pluck an element
* from the array and place it to its right place.
* Time Complexity of the insertion sort algorithm is O(n2) in the worst case and O(n)
* in the best case.
*
* It is a stable algorithm since it preserves the order of equal elements.
*
* It is not a recursive algorithm.
*
* Insertion sort is adaptive by default and no extra effort is needed to make it adaptive.
* The time complexity itself gets reduced from O(n2) to O(n) when the algorithm finds an
* array already sorted.

"""


class InsertionSortAlgorithm:

    # method to traverse and print array element
    def print_array(self, n, arr):

        for i in range(0, n):
            print(arr[i], end=" ")
        print()

    # implenent insertion sort logic using two for loops
    def insert_sort_logic(self, n, arr):

        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if(arr[j] > arr[j+1]):
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp

    # implenent insertion sort logic using for-while loop
    def insert_sort_logic2(self, n, arr):

        for i in range(1, n):  # iterate all the elements

            j = i-1
            # keep shifting the smaller element to left until it reaches right position
            while(j >= 0 and arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                j = j-1


# driver code
if __name__ == "__main__":

    print("Please  enter the array elements separated by a space: ", end="\n")

    arr = list(map(int, input().split()))

    n = len(arr)

    # create InsertionSortAlgorithm class instance
    sorting = InsertionSortAlgorithm()

    print("The array elements before sorting: ", end=" ")
    sorting.print_array(n, arr)

    # sorting.insert_sort_logic(n,arr)
    sorting.insert_sort_logic2(n, arr)
    print("The array elements after sorting: ", end=" ")
    sorting.print_array(n, arr)
