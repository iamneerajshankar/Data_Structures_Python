"""
* In selection sort, at each pass, we make sure that the smallest element of the current
 * unsorted sub-array reaches its final position. And this is pursued by finding the smallest
 * element in the unsorted sub-array and replacing it at the end with the element at the first
 * index of the unsorted sub-array.
 *
 * The time complexity of the selection sort algorithm is O(n2) in all its cases.
 * It is not a stable algorithm since it fails to preserve the original order of equal elements.
 * We saw one example the other day.
 *
 * It is not a recursive algorithm.
 * Selection sort is not an adaptive algorithm. It anyway makes comparisons regardless of whether the
 * array given is sorted or not.
"""


class SelectionSortAlgorithm:
    # method to traverse and print array element
    def print_array(self, n, arr):

        for i in range(0, n):
            print(arr[i], end=" ")
        print()

    def selection_sort(self, n, arr):

        for i in range(0, n):
            indexOfMin = i
            for j in range(i+1, n):
                if(arr[j] < arr[indexOfMin]):
                    indexOfMin = j  # // keep track of index of minimum element at each iteration

            temp = arr[i]
            arr[i] = arr[indexOfMin]
            arr[indexOfMin] = temp


# driver code

if __name__ == "__main__":

    print("Please enter the array elements separated by space: ", end="\n")
    arr = list(map(int, input().split()))
    n = len(arr)
    # create InsertionSortAlgorithm class instance
    sorting = SelectionSortAlgorithm()

    print("The array elements before sorting: ", end=" ")
    sorting.print_array(n, arr)

    sorting.selection_sort(n, arr)
    print("The array elements after sorting: ", end=" ")
    sorting.print_array(n, arr)
