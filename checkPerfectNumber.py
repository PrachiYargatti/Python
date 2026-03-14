class solution:
    def checkPerfectNumber(self, num):
        #Write your code here...
        divisors = []
        
        for i in range(1, int(num**0.5)+1):
            if num%i == 0:
                divisors.append(i)
                if i != num//i and num//i != num:
                    divisors.append(num//i)
        
        if sum(divisors) == num:
            return True
        return False

# Time Complexity : O(√n)
# Space Complexity : O(√n)
