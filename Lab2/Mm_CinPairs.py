# Maximum and minimum of an array by comparing in pairs
def getMinMax(arr):
    n = len(arr)
    
    # If array has even number of elements
    if n % 2 == 0:
        if arr[0] < arr[1]:
            mn = arr[0]
            mx = arr[1]
        else:
            mn = arr[1]
            mx = arr[0]
        i = 2
    else:
        mn = mx = arr[0]
        i = 1
    
    # Process elements in pairs
    while i < n - 1:
        if arr[i] < arr[i + 1]:
            mx = max(mx, arr[i + 1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i + 1])
        i += 2
    
    return mx, mn

if __name__ == '__main__':
    arr = [1000, 11, 445, 1, 330, 3000]
    mx, mn = getMinMax(arr)
    print('Minimum element is', mn)
    print('Maximum element is', mx)
