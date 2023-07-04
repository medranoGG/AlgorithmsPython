
N, M = map(int, input().strip().split())


def select_next_drone(distances, visited):
    best_drone = -1
    best_dist = float('Inf')
    for drone in range(len(visited)):
        if not visited[drone] and distances[drone] < best_dist:
            best_drone = drone
            best_dist = distances[drone]
    return best_drone, best_dist


def calc_drones_info(drones):
    n = len(drones)
    init_drone = 0
    visited = [False] * n
    distances = [float('Inf')] * n
    visited[init_drone] = True
    total_weight = 0
    drone_info = []
    prev_drone = [-1] * n
    for _ in range(n):
        drone_dict = {
            'node_list': [],
            'total_drone_cost': 0
        }
        drone_info.append(drone_dict)
    for start, end, weight in drones[init_drone]:
        distances[end] = weight
        prev_drone[end] = start
    for _ in range(1, n):
        next_drone, next_dist = select_next_drone(distances, visited)
        if next_dist < float('Inf'):
            visited[next_drone] = True
            total_weight += next_dist
            drone_info[next_drone]['node_list'].append(prev_drone[next_drone])
            drone_info[next_drone]['total_drone_cost'] += next_dist
            drone_info[prev_drone[next_drone]]['node_list'].append(next_drone)
            drone_info[prev_drone[next_drone]]['total_drone_cost'] += next_dist
            for start, end, weight in drones[next_drone]:
                if weight < distances[end]:
                    distances[end] = weight
                    prev_drone[end] = start
    return total_weight, drone_info


dr = []
for _ in range(N):
    dr.append([])

for _ in range(M):
    U, V, W = map(int, input().strip().split())
    dr[U].append([U, V, W])
    dr[V].append([V, U, W])

C = int(input())
ask_drones = []
for _ in range(C):
    ask_drones.append(int(input()))


total_cost, dr_info = calc_drones_info(dr)
print(total_cost)
for d in ask_drones:
    dr_info[d]['node_list'].sort()
    print("{0}:".format(dr_info[d]['total_drone_cost']), *dr_info[d]['node_list'])
