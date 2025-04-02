def array_sum_recursive(arr, n):
    # Base case: If the array is empty, return 0
    if n == 0:
        return 0
    # Recursive case: Sum the current element with the sum of the rest of the array
    return arr[n - 1] + array_sum_recursive(arr, n - 1)

# Example usage:
my_array = [1, 2, 3, 49, 6.9]
array_size = len(my_array)

result_sum = array_sum_recursive(my_array, array_size)

print("Array:", my_array)
print("Sum of all elements:", result_sum)
