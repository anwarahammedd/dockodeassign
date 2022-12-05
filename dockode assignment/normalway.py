n = int(input("n:"))
m = int(input("m:"))

matrix = [[0 for j in range(m)] for i in range(n)]

number = 1
for i in range(n):
    for j in range(m):
        matrix[i][j] = number
        number += 1

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=" ")
    print()
