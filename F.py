
def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count = count+1
    return count

# Example usage
array = [0, 5, 5, 5, 4]
element = 5
result = count_occurrences(array, element)
print(f"The element {element} appears {result} times in the array.")
