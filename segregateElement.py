class Solution:
    def segregateElements(self, arr):
        left = 0
        right = 0
        n = len(arr)
        
        while right < n:
            if arr[right] < 0:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
            right += 1

s=Solution()
s.segregateElements([3,2,-1,3,-7])
#output-->[-1,-7,2,3,3]

