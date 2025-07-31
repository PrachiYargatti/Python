n = int(input("enter number: "))
original = n 
reversed = 0

while n>0:
    digit = n%10
    reversed = reversed*10 + digit 
    n = n//10

if(original == reversed):
    print(f"{original} number is a palindrome")
else:
    print(f"{original} number is not a palindrome")
