def print_anti_diagonals(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for k in range(m + n - 1):
        for i in range(max(0, k - n + 1), min(k + 1, m)):
            j = k - i
            print(matrix[i][j], end=" ")
        print()

m,n=input().split()
m,n=int(m),int(n)

matrix = []
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

print_anti_diagonals(matrix)
