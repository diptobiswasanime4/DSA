def min_sum(x, y, matrix, n, memo):
    if x == n:
        return 0
    if y > 0 and y < n - 1:
        res1 = matrix[x][y] + min_sum(x + 1, y - 1, matrix, n, memo)
        res2 = matrix[x][y] + min_sum(x + 1, y, matrix, n, memo)
        res3 = matrix[x][y] + min_sum(x + 1, y + 1, matrix, n, memo)
        return min([res1, res2, res3])
    elif y == 0:
        res2 = matrix[x][y] + min_sum(x + 1, y, matrix, n, memo)
        res3 = matrix[x][y] + min_sum(x + 1, y + 1, matrix, n, memo)
        return min([res2, res3])    
    elif y == n - 1:
        res1 = matrix[x][y] + min_sum(x + 1, y - 1, matrix, n, memo)
        res2 = matrix[x][y] + min_sum(x + 1, y, matrix, n, memo)
        return min([res1, res2])

if __name__ == "__main__":
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    n = len(matrix)

    min_list = []
    for i in range(n):
        res = min_sum(0, i, matrix, n, {})
        min_list.append(res)
    
    print(min(min_list))