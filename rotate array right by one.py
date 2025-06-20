class Solution:
    def rotate(self, arr):
        self.reverse(arr, 0, len(arr) - 1)    #[5,4,3,2,1]
        self.reverse(arr, 1, len(arr) - 1)    #[5,1,2,3,4]

    def reverse(self, arr, i, j):            
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1


arr = [1, 2, 3, 4, 5]
s = Solution()
s.rotate(arr)

#output-->[5,1,2,3,4]
