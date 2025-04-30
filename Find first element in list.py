def get_index(numbers_list, number):
     # Complete this recursive function
    for i in range(len(numbers_list)):
        numbers_list[i]=int(numbers_list[i])
        if numbers_list[i]==number:
            return i
            break


numbers_list = input().split()
number = int(input())


number_index = get_index(numbers_list, number)# Call the get_index function

print(number_index)
