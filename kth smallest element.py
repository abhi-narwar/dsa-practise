import heapq  # To use heap (priority queue)  --->heapq supports only min_heap, to make max_heap we take negative values  and we pop maximum element from the top of heap if array size>k .

class Solution:
    def kthSmallest(self, arr, K):
        # Step 1: Create an empty list that will act like a max-heap
        max_heap = []

        # Step 2: Traverse each number in the array
        for num in arr:
            # Push the negative of the number (to simulate max-heap using min-heap)
            heapq.heappush(max_heap, -num)

            # Step 3: If the heap has more than K elements, remove the largest (which is the smallest in negative)
            if len(max_heap) > K:
                heapq.heappop(max_heap)

        # Step 4: After processing all elements, the root of the heap is the Kth smallest
        # Convert it back to positive before returning
        return -max_heap[0]
        
s=Solution()
s.kthSmallest([7,10,4,3,20,15],3)

#output:7
