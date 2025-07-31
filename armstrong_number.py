# armstrong 
number = input("enter the number: ")
power = len(number)
sum = 0

for digit in number:
    sum += int(digit)**power
    
if(sum == int(number)):
    print(f"{number} is an armstrong number") #153
else:
    print(f"{number} is not an armstrong number")
