import heapq

def kth_largest(arr, k):
    min_heap = []

    for num in arr:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]

# Example
arr = [12, 5, 787, 1, 23]
k = 3
print(kth_largest(arr, k))  # Output: 23
