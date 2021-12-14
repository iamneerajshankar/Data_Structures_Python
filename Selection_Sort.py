def selection_sort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:  # compare the array at min_indth = stepth with array at ith index
                min_idx = i
        # swap the element between array step(stop holds outer loop value) and array at min_idx in outer loop
        (array[step], array[min_idx]) = (array[min_idx], array[step])


# driver code
print("Please enter the size of the array: ")
size = int(input())
data_list = []
print("Please enter the elements of the array: ")
for i in range(size):
    data = int(input())
    data_list.append(data)

selection_sort(data_list, size)
print("The array in the sorted form: ")
print(data_list)
