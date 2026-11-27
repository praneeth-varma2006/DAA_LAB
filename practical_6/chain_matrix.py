def matrix_chain_order(p, n):
    m = [[0 for i in range(n)] for j in range(n)]

    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = float('inf')

            for k in range(i, j):
                cost = (m[i][k] + m[k + 1][j] +
                        p[i - 1] * p[k] * p[j])

                if cost < m[i][j]:
                    m[i][j] = cost

    return m[1][n - 1]


n = int(input("Enter number of matrices: "))

p = []

print("Enter dimensions:")

for i in range(n + 1):
    x = int(input())
    p.append(x)

result = matrix_chain_order(p, n + 1)

print("Minimum number of multiplications:", result)