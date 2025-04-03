def array_sum_recursive(arr):
    # Base case: If the array is empty, return 0
    if not arr:
        return 0
    # Recursive case: Sum the current element with the sum of the rest of the array
    return arr[0] + array_sum_recursive(arr[1:])

# Example usage:
my_array = [1.1, 3, 9, 49, 6.9]

result_sum = array_sum_recursive(my_array)

print("Array:", my_array)
print("Sum of all elements:", result_sum)
