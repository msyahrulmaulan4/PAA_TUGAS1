import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, distance):
        self._add_edge(from_node, to_node, distance)
        self._add_edge(to_node, from_node, distance)

    def _add_edge(self, from_node, to_node, distance):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

    def dijkstra(self, start_node):
        distances = {node: float('inf') for node in self.nodes}
        distances[start_node] = 0
        pq = [(0, start_node)]
        while pq:
            current_distance, current_node = heapq.heappop(pq)
            if current_distance > distances[current_node]:
                continue
            if current_node in self.edges:
                for neighbor in self.edges[current_node]:
                    distance = current_distance + self.distances[(current_node, neighbor)]
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(pq, (distance, neighbor))
        return distances

# Contoh penggunaan algoritma Dijkstra untuk sistem pengelolaan rute pengiriman barang
route_graph = Graph()
route_graph.add_node("Jakarta")
route_graph.add_node("Surabaya")
route_graph.add_node("Bandung")
route_graph.add_node("Yogyakarta")

route_graph.add_edge("Jakarta", "Surabaya", 500)
route_graph.add_edge("Jakarta", "Bandung", 150)
route_graph.add_edge("Surabaya", "Bandung", 300)
route_graph.add_edge("Surabaya", "Yogyakarta", 400)
route_graph.add_edge("Bandung", "Yogyakarta", 250)

# Menentukan rute terpendek antara Jakarta dan Yogyakarta
distances = route_graph.dijkstra("Jakarta")
shortest_distance = distances["Yogyakarta"]
print("Jarak terpendek antara Jakarta dan Yogyakarta:", shortest_distance)

# Menampilkan rute terpendek dari Jakarta ke Yogyakarta
current_node = "Yogyakarta"
route = []
while current_node != "Jakarta":
    route.append(current_node)
    neighbors = route_graph.edges[current_node]
    for neighbor in neighbors:
        if distances[neighbor] + route_graph.distances[(current_node, neighbor)] == distances[current_node]:
            current_node = neighbor
            break
route.append("Jakarta")
route.reverse()
print("Rute terpendek dari Jakarta ke Yogyakarta:", ' -> '.join(route))

