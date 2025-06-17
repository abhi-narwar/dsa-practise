class Solution:
    def get_min_max(self, arr):
        min_value=float('inf')
        max_value=float('-inf')
        
        for val in arr:
            if val<min_value:
                min_value=val
            if val>max_value:
                max_value=val
        return [min_value,max_value]
s=Solution()
s.get_min_max([1,2,5,3])

#output :
#[min_value,max_value]-->[1,5]
            
        
        
        
    
