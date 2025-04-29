# Maximum and minimum of an array using Linear search
def find_max(arr):
    if len(arr) == 0:
        return None

    # Initialize max value with the first element
    max_val = arr[0]

    # Iterate through the array
    for num in arr:
        if num > max_val:
            max_val = num

    return max_val

def find_min(arr):
    if len(arr) == 0:
        return None

    # Initialize min value with the first element
    min_val = arr[0]

    # Iterate through the array
    for num in arr:
        if num < min_val:
            min_val = num

    return min_val

# Example usage:
arr = [3, 1, 8, 4, 9, 2]
max_val = find_max(arr)
min_val = find_min(arr)
print("Maximum:", max_val)
print("Minimum:", min_val)
