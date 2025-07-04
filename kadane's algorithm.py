class Solution:
    def maxSubarraySum(self, arr):
        curr_sum=arr[0]
        max_sum=arr[0]
        for i in range(1,len(arr)):
            curr_sum=max(curr_sum+arr[i],arr[i])
            max_sum=max(curr_sum,max_sum)
        return max_sum
