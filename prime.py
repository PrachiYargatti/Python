n = int(input("enter number: "))
isPrime = True

if n<=1:
    isPrime = False 
else:
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            isPrime = False 
            
if(isPrime):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
