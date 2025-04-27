# Greedy approach for job sequencing problem
def printJobScheduling(arr, t):
    # Length of array
    n = len(arr)

    # Sort all jobs according to decreasing order of profit
    arr.sort(key=lambda x: x[2], reverse=True)

    # To keep track of free time slots
    result = [False] * t

    # To store result (Sequence of jobs)
    job = ['-1'] * t

    # Iterate through all given jobs
    for i in range(n):
        # Find a free slot for this job (Note that we start from the last possible slot)
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            # Free slot found
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break

    # Print the sequence
    print(job)

# Driver Code
if __name__ == "__main__":
    arr = [['a', 2, 100],  # Job Array
           ['b', 1, 19],
           ['c', 2, 27],
           ['d', 1, 25],
           ['e', 3, 15]]

    print("Following is the maximum profit sequence of jobs:")
    # Function Call
    printJobScheduling(arr, 3)
