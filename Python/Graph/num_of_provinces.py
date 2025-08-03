n = 9
edges = [[1, 0], [1, 2], [1, 3], [2, 3], [2, 4], [3, 5], [4, 5], [6, 7]]

adj_matrix = []
for i in range(n):
    row = []
    for i in range(n):
        row.append(False)
    adj_matrix.append(row)
for edge in edges:
    x, y = edge
    adj_matrix[x][y] = True
    adj_matrix[y][x] = True

vis_arr = []
for i in range(n):
    vis_arr.append(False)

def bfs(src, adj_matrix, vis_arr):
    queue = []
    queue.append(src)
    vis_arr[src] = True

    while len(queue) > 0:
        cur = queue.pop()

        for i in range(n):
            if adj_matrix[cur][i] and not vis_arr[i]:
                vis_arr[i] = True
                queue.append(i)

provinces = 0

for i in range(n):
    if not vis_arr[i]:
        bfs(i, adj_matrix, vis_arr)
        provinces += 1
        print(vis_arr)


print(provinces)