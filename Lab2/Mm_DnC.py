# Find maximum and minimum elements from an array of integers using divide and concurrent strategy.
def max_min_devide_conquer(arr, low, high):
    class Pair:
        def __init__(self):
            self.max = float('-inf')
            self.min = float('inf')
    
    result = Pair()
    
    # If there's only one element
    if low == high:
        result.max = arr[low]
        result.min = arr[low]
        return result
    
    # If there are two elements
    if high == low + 1:
        if arr[low] > arr[high]:
            result.max = arr[low]
            result.min = arr[high]
        else:
            result.max = arr[high]
            result.min = arr[low]
        return result
    
    # If there are more than two elements
    mid = (low + high) // 2
    left_result = max_min_devide_conquer(arr, low, mid)
    right_result = max_min_devide_conquer(arr, mid + 1, high)

    # Combine the results
    result.max = max(left_result.max, right_result.max)
    result.min = min(left_result.min, right_result.min)

    return result

# Example usage
arr = [6, 4, 26, 14, 33, 64, 46]
result = max_min_devide_conquer(arr, 0, len(arr) - 1)
print("Maximum element is:", result.max)
print("Minimum element is:", result.min)
