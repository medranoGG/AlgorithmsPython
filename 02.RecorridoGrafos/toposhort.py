from collections import deque
def toposort_visit(k, data):
    data["state"][k] = "VISITED"
    data["time"] += 1
    data["discover"][k] = data["time"]

    for adj in data["graph"][k]:
        if data["state"][adj] == "NOT VISITED":
            toposort_visit(adj, data)
            data["state"][k] = "FINISHED"
            data["time"] += 1
            data["finish"][k] = data["time"]
            data["sol"].appendleft(k)
def toposort(g):
    data = {
        "graph": g,
        "state": dict(),
        "discover": dict(),
        "finish": dict(),
        "time": 0,
        "sol": deque()
    }

    for k in g.keys():
        data["state"][k] = "NOT VISITED"
        data["discover"][k] = 0
        data["finish"][k] = 0

    for k in g.keys():
        if data["state"][k] == "NOT VISITED":
            toposort_visit(k, data)

    print(data["sol"])


if __name__ == '__main__':

    graph = {
        "calcetines": ["zapatos"],
        "pantalon": ["zapatos", "cinturon"],
        "camisa": ["cinturon", "jersey"],
        "zapatos": [],
        "cinturon": [],
        "jersey": []
    }

    toposort(graph)