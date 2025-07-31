str = input("enter the string: ")
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_count = 0 
for chr in str:
    if chr in vowels:
        vowels_count += 1 
        
print(f"vowels count in the string {str} is {vowels_count}")
