def heapify(arr, n, i):
    # 루트를 구하고 왼쪽과 오른쪽 자식 노드를 찾는다.
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # 왼쪽 자식이 존재하고 값이 루트보다 크면 largest를 왼쪽 자식 인덱스로 설정
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 존재하고 값이 largest보다 크면 largest를 오른쪽 자식 인덱스로 설정
    if right < n and arr[right] > arr[largest]:
        largest = right

    # largest가 루트와 다르면 largest와 루트를 교환하고 largest를 기준으로 heapify 재귀 호출
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # 최대 힙 구축
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # 힙을 구축했으므로 루트 노드와 마지막 노드를 교환한 후 힙을 재구축
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# 예시 배열
arr = [12, 11, 13, 5, 6, 7]

heap_sort(arr)
print("정렬된 배열:", arr)