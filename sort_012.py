class Solution:
    
    def sort012(self, arr):
        i=0
        j=0
        k=len(arr)-1
        while (i<=k):                                      """it is solved using dutch national flag algorithm 
            if arr[i]==0:                                   i represent starting index
                arr[j],arr[i]=arr[i],arr[j]                 j put the element in sorted manner in same array according to element order like 0,0,1,1,2,2 .
                i+=1                                        k represent end of array """
                j+=1
            elif arr[i]==1:
                i+=1
            else:
                arr[i],arr[k]=arr[k],arr[i]
                k-=1
s=Solution()
s.sort012([0,1,2,0,1,2])
    
            
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
