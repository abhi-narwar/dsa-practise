class Solution:    
    def findUnion(self, a, b):
       a.extend(b)
       res=len(set(a))
       return res
s=Solution()
s.findUnion([1,2,3,4,5],[1,2,3])
#output-->5
