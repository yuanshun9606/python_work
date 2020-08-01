def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if (cost < lowest_cost) & (node not in processed):
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 邻接列表表示图结构，与邻接集合的操作相同
graph = {"start": {'a': 6, 'b': 2},
         'a': {'fin': 1},
         'b': {'a': 3, 'fin': 5},
         'fin': {}}

inf = float("inf")
costs = {"a": 6, "b": 2, "fin": inf}
parent = {"a": "start", "b": "start", "fin": None}
processed = []

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parent[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs["fin"])

