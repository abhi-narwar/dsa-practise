class Solution:
    def intersectionWithDuplicates(self, a, b):
        # code here
        return list(set(a)&set(b))
                
        
        
s=Solution()
s.intersectionWithDuplicates([1,2,1,3,1],[3,1,3,4,1])

#output-->[1,3]
