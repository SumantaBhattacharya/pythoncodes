def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
my_list = [69, 68, 9, 77, 404, 6.9, 99, 420, 104]

print("Original array:", my_list)

bubble_sort(my_list)

print("Sorted array:", my_list)
