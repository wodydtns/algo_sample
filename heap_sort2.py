import heapq


def heap_sort(arr):
    heap = [-x for x in arr]  # 최대 힙으로 변환
    heapq.heapify(heap)  # 힙 생성

    sorted_arr = []

    # 힙에서 최대값을 꺼내 정렬된 배열에 추가
    for _ in range(len(arr)):
        sorted_arr.append(-heapq.heappop(heap))

    return sorted_arr


# 예시 배열
arr = [12, 11, 13, 5, 6, 7]

print("정렬된 배열:", heap_sort(arr))
