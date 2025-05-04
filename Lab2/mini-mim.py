# * Find Maximum and minimum of an array using mini- mum number of comparisons.
def find_max_min(arr):
    if len(arr) == 0:
        return None, None
    if len(arr) == 1:
        return arr[0], arr[0]

    # Initialize max and min values
    max_val = arr[0]
    min_val = arr[0]

    # Compare in pairs
    for i in range(1, len(arr) - 1, 2):
        if arr[i] < arr[i + 1]:
            max_val = max(max_val, arr[i + 1])
            min_val = min(min_val, arr[i])
        else:
            max_val = max(max_val, arr[i])
            min_val = min(min_val, arr[i + 1])

    # If the array length is odd, handle the last element separately
    if len(arr) % 2 != 0:
        max_val = max(max_val, arr[-1])
        min_val = min(min_val, arr[-1])

    return min_val, max_val

# Example usage:
arr = [3, 1, 8, 4, 9, 2]
min_val, max_val = find_max_min(arr)
print("Maximum:", max_val)
print("Minimum:", min_val)
