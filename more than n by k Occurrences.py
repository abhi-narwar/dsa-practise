class Solution:
    
    # Function to find all elements in array that appear more than n/k times.
    def countOccurence(self, arr, k):
        n = len(arr)
        freq = {}
        
        # Count the frequency of each element
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        # Count how many elements appear more than n/k times
        count = 0
        for value in freq.values():
            if value > n // k:
                count += 1
        
        return count
