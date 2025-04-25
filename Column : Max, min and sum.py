def get_transpose_of_matrix(matrix, m, n):
    # Complete this function
    Transpose=[]
    for i in range(n):
        innerlist=[]
        for j in range(m):
            innerlist.append(matrix[j][i])
        Transpose.append(innerlist)
    return Transpose

def print_max_min_sum_for_row_wise(num_list):
    # Complete this function
    Max=[]
    Min=[]
    Sum=[]
    for i in num_list:
        Max.append(max(i))
        Min.append(min(i))
        Sum.append(sum(i))
    print(Max)
    print(Min)
    print(Sum)

def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)
Transpose=get_transpose_of_matrix(num_list,m,n)
print_max_min_sum_for_row_wise(Transpose)
# Write your code here
# Call the get_transpose_of_matrix function
# Call the print_max_min_sum_for_row_wise function
