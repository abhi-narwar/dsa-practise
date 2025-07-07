class Solution:
    def factorial(self, n):
        fact = 1
        
        # Compute factorial
        for i in range(2, n + 1):
            fact *= i
        
        # Convert factorial to list of digits
        return [int(j) for j in str(fact)]
#5--->[1,2,0]
