# Maximum and minimum of an array using Linear
def find_max_min(arr):
    if len(arr) == 0:
        return None, None
    if len(arr) == 1:
        return arr[0], arr[0]

    # Initialize max and min values with the first element
    max_val = arr[0]
    min_val = arr[0]

    # Iterate through the array
    for num in arr:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num

    return max_val, min_val

# Example usage:
arr = [3, 1, 8, 4, 9, 2]
max_val, min_val = find_max_min(arr)
print("Maximum:", max_val)
print("Minimum:", min_val)
