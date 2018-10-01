# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

def diagonal(matrix):
  m = len(matrix)    
  if m > 0:
      n = len(matrix[0])
      results = []
      for k in range(m+n-1):
          if k % 2 == 0:
            i = min(k, m-1)
            j = max(0, k-m+1)
            while i >= 0 and j < n:
              results.append(matrix[i][j])
              i -= 1
              j += 1
          else:
            i = max(0, k-n+1)
            j = min(k, n-1)
            while j >= 0 and i < m:
              results.append(matrix[i][j])
              i += 1
              j -= 1
      return results
  else:
      return []

print(diagonal([[1,2,3,4],[5,6,7,8], [9,10,11,12]]))

