import copy

def bfs_list(n, adj_list, vis_arr, src, dst):
    queue = []
    queue.append(src)
    vis_arr[src] = True

    while len(queue) > 0:
        cur = queue.pop()

        if cur == dst:
            return True
        
        for neighbor in adj_list[cur]:
            if not vis_arr[neighbor]:
                vis_arr[neighbor] = True
                queue.append(neighbor)

    return False


def dfs_list(n, adj_list, vis_arr, src, dst):
    if src == dst:
        return True
    
    for neighbor in adj_list[src]:
        if not vis_arr[neighbor]:
            vis_arr[neighbor] = True
            if dfs_list(n, adj_list, vis_arr, neighbor, dst):
                return True
    
    return False


def bfs_matrix(n, adj_matrix, vis_arr, src, dst):
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


def dfs_matrix(n, adj_matrix, vis_arr, src, dst):
    if src == dst:
        return True
    
    for i in range(n):
        if adj_matrix[src][i] and not vis_arr[i]:
            vis_arr[i] = True
            if dfs_matrix(n, adj_matrix, vis_arr, i, dst):
                return True
    return False


def is_valid_path(n, edges, src, dst):
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
    
    return [dfs_matrix(n, adj_matrix, copy.deepcopy(vis_arr), src, dst), bfs_matrix(n, adj_matrix, copy.deepcopy(vis_arr), src, dst), dfs_list(n, adj_list, copy.deepcopy(vis_arr), src, dst), bfs_list(n, adj_list, copy.deepcopy(vis_arr), src, dst)]


if __name__ == "__main__":
    #default
    n = 7
    edges = [[0,1],[1,2],[2,3],[1,3],[4,5],[5,6],[4,6]]
    src = 0
    dst = 3
    
    # n = 10
    # edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
    # src = 5
    # dst = 9

    print(is_valid_path(n, edges, src, dst))
