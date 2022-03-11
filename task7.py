#Task 7
#Develop a procedure that will have a size argument and print a table where num of  #columns and rows will be of this size. Cells of table should contain numbers from 1 to n ** 2 placed in a spiral fashion. Spiral should start from top left cell and has a clockwise direction (see the example below).

n = int(input())
a = [[0 for i in range(n)] for j in range(n)]
k = 1
m = 0
while k <= n*n:
    for i in range(m, n-m):
        a[m][i]= k
        k += 1
    for i in range(m+1, n-m):
        a[i][n-m-1]= k
        k += 1
    for i in range(n-m-2, m-1, -1):
        a[n-m-1][i] = k
        k += 1
    for i in range(n-2-m,m, -1):
        a[i][m] = k
        k += 1
    m += 1
for i in range(n):
    for j in range(n):
        print(a[i][j], end =' ')
    print()
