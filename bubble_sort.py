array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
n = len(array)
for i in range(n):
    for j in range(0, n - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
