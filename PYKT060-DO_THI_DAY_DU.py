def input_graph():
    n = int(input())
    m = int(input())

    adj = [[0] * (n + 1) for _ in range(n + 1)]
    parent = [-1] * (n + 1)
    zones = []

    for _ in range(m):
        u, v = map(int, input().split())
        adj[u][v] = adj[v][u] = 1

        if parent[u] == -1 and parent[v] == -1:
            zone_id = len(zones)
            zones.append(set([u, v]))
            parent[u] = parent[v] = zone_id
        elif parent[u] != -1 and parent[v] == -1:
            zones[parent[u]].add(v)
            parent[v] = parent[u]
        elif parent[v] != -1 and parent[u] == -1:
            zones[parent[v]].add(u)
            parent[u] = parent[v]
        elif parent[u] != parent[v]:
            # Gộp hai zone nếu u và v khác zone
            id_u = parent[u]
            id_v = parent[v]
            if len(zones[id_u]) < len(zones[id_v]):
                id_u, id_v = id_v, id_u
            zones[id_u].update(zones[id_v])
            for node in zones[id_v]:
                parent[node] = id_u
            zones[id_v].clear()

    return n, adj, zones


def is_valid_clique(zones, adj):
    for group in zones:
        nodes = list(group)
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                u, v = nodes[i], nodes[j]
                if adj[u][v] == 0:
                    return False
    return True


def main():
    n, adj, zones = input_graph()
    if is_valid_clique(zones, adj):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
