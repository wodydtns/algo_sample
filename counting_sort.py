# 계수 정렬
def counting_sort(arr):
    # Find the maximum element in the array to determine the range of the count array
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Create count array and initialize all elements to 0
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Store the count of each element in count array
    for i in range(0, len(arr)):
        count[arr[i] - min_val] += 1

    # Change count[i] so it contains the actual position of this element in the output array
    for i in range(1, range_of_elements):
        count[i] += count[i - 1]

    # Build the output array by placing elements at their correct positions
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    # Copy the sorted elements into the original array
    for i in range(0, len(arr)):
        arr[i] = output[i]


# Example usage
if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1]
    counting_sort(arr)
    print("Sorted array is:", arr)
