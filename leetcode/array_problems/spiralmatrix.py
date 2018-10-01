def spiral(matrix):
    m = len(matrix)
    results = []
    if m > 0:
        n = len(matrix[0])
        k = l = 0
        while k < m and l < n:
            for i in range(l,n):
                results.append(matrix[k][i])
            k += 1
            for j in range(k, m):
                results.append(matrix[j][n-1])
            n -= 1
            if (k<m):
                for i in range(n-1,l-1,-1):
                    results.append(matrix[m-1][i])
                m -= 1
            if (l<n):
                for j in range(m-1, k-1, -1):
                    results.append(matrix[j][l])
                l += 1
    return results

print(spiral([[1,2,3],[4,5,6],[7,8,9]]))