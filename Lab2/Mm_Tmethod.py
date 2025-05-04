# Maximum and minimum of an array using the tournament method.
def getMinMax(low, high, arr):
    if low == high:
        # Only one element
        return arr[low], arr[low]

    elif high == low + 1:
        # Two elements
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    else:
        # More than two elements
        mid = (low + high) // 2
        arr_max1, arr_min1 = getMinMax(low, mid, arr)
        arr_max2, arr_min2 = getMinMax(mid + 1, high, arr)

        arr_max = max(arr_max1, arr_max2)
        arr_min = min(arr_min1, arr_min2)

        return arr_max, arr_min

# Example usage
arr = [1000, 11, 445, 1, 330, 3000]
high = len(arr) - 1
low = 0
arr_max, arr_min = getMinMax(low, high, arr)
print('Minimum element is', arr_min)
print('Maximum element is', arr_max)

# Maximum element is 1
# nMaximum element is 3000
      