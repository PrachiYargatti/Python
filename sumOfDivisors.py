class solution:
    def sumOfDivisors(self, num):
        #Write your code here...
        divisors = []
        
        for i in range(1, int(num**0.5)+1): 
            if num%i == 0:
                divisors.append(i)
                if i != num//i:
                    divisors.append(num//i)
        
        return sum(divisors)

# space complexity: O(sqrt(n))
# time complexity: O(sqrt(n))
            
