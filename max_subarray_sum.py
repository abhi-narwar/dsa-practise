class Solution:                                '''in this question we use kadane's algorithm 
    def maxSubArraySum(self, arr):                 here we use two variaable 
        c_sum=arr[0]                               current_sum,maximum_sum
        m_sum=arr[0]
        for i in range(1,len(arr)):            '''
            c_sum=max(c_sum+arr[i],arr[i])
            m_sum=max(c_sum,m_sum)
        return m_sum
s = Solution()
s.maxSubArraySum( [2, 3, -8, 7, -1, 2, 3])

#output:11
