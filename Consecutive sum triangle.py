def sum_of_consecutive_elements(num_list):
    end_index = len(num_list) - 1
    result = []
    for i in range(end_index):
        s = num_list[i] + num_list[i+1]
        result.append(s)
    return result
    
def print_sum_list(num_list):
    while len(num_list) > 1:
        con_sum = sum_of_consecutive_elements(num_list)
        print(con_sum)
        num_list = con_sum

def convert_str_to_int(string):
    new_list = []
    for i in string:
        num = int(i)
        new_list.append(num)
    return new_list

string = input().split(",")
num_list = convert_str_to_int(string)
print(num_list)
print_sum_list(num_list)
