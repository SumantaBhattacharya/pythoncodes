
# * maximum and minimum of an array using sorting.
def find_max_min(arr):
    if len(arr) == 0:
        return None, None
    if len(arr) == 1:
        return arr[0], arr[0]

    # Sort the array
    arr.sort()

    # First element is the minimum
    min_val = arr[0]

    # Last element is the maximum
    max_val = arr[-1]

    return min_val, max_val

# Example usage:
arr = [3, 1, 8, 4, 9, 2]
min_val, max_val = find_max_min(arr)
print("Maximum:", max_val)
print("Minimum:", min_val)
# C:\Users\Sumanta Bhattacharya\OneDrive\Documents\Desktop\pythoncodes\Lab2\Array_sorting.py