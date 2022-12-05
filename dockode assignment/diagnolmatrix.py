n = int(input("n:"))
m = int(input("m:"))

matrix = [[0 for j in range(m)] for i in range(n)]
number = 1
for i in range(n):
    for j in range(m):
        matrix[i][j] = number
        number += 1

for j in range(m):
    i = 0
    k = j
    while k >= 0:
        print(matrix[i][k], end=" ")
        i += 1
        k -= 1
    print()
for i in range(1, n):
    j = m - 1
    k = i
    while k < n:
        print(matrix[k][j], end=" ")
        k += 1
        j -= 1
    print()