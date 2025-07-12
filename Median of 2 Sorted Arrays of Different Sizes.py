class Solution:
    def medianOf2(self, a, b):
        merged_arr = a + b             
        merged_arr.sort()              
        n = len(merged_arr)
        
        if n % 2 == 1:
            return merged_arr[n // 2]  # Odd case
        else:
            mid1 = merged_arr[n // 2]
            mid2 = merged_arr[(n // 2) - 1]
            return (mid1 + mid2) / 2   # Even case
