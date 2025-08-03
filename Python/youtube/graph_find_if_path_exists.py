import copy

def bfs_list(src, dst, n, adj_list, vis_arr):
    queue = []
    queue.append(src)

    vis_arr[src] = True

    while len(queue) > 0:
        cur = queue.pop()

        if cur == dst:
            return True
        
        for neighbor in adj_list[cur]:
            if not vis_arr[neighbor]:
                queue.append(neighbor)
                vis_arr[neighbor] = True
    
    return False

def bfs_matrix(src, dst, n, adj_matrix, vis_arr):
    queue = []
    queue.append(src)

    vis_arr[src] = True

    while len(queue) > 0:
        cur = queue.pop()

        if cur == dst:
            return True
        
        for i in range(n):
            if adj_matrix[cur][i] and not vis_arr[i]:
                queue.append(i)
                vis_arr[i] = True
    
    return False


def dfs_list(src, dst, n, adj_list, vis_arr):
    if src == dst:
        return True
    
    for neighbor in adj_list[src]:
        if not vis_arr[neighbor]:
            vis_arr[neighbor] = True
            if (dfs_list(neighbor, dst, n, adj_list, vis_arr)):
                return True
    return False


def dfs_matrix(src, dst, n, adj_matrix, vis_arr):
    if src == dst:
        return True

    for i in range(n):
        if adj_matrix[src][i] and not vis_arr[i]:
            vis_arr[i] = True
            if (dfs_matrix(i, dst, n, adj_matrix, vis_arr)):
                return True
    return False


n = 10
edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
src = 5
dst = 9

#Adj Matrix
adj_matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(False)
    adj_matrix.append(row)

for edge in edges:
    x, y = edge
    adj_matrix[x][y] = True
    adj_matrix[y][x] = True

#Adj List
adj_list = []
for i in range(n):
    row = []
    adj_list.append(row)

for edge in edges:
    x, y = edge
    adj_list[x].append(y)
    adj_list[y].append(x)

vis_arr = []
for i in range(n):
    vis_arr.append(False)

print(dfs_matrix(src, dst, n, adj_matrix, copy.deepcopy(vis_arr)))
print(dfs_list(src, dst, n, adj_list, copy.deepcopy(vis_arr)))
print(bfs_matrix(src, dst, n, adj_matrix, copy.deepcopy(vis_arr)))
print(bfs_list(src, dst, n, adj_list, copy.deepcopy(vis_arr)))


