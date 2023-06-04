import node as Node
import random

class Network:
    def __init__(self, nodes_number, neighbor_per_node, process_time, sending_time, routing_mode):
        self.nodes_number = nodes_number
        self.neighbor_per_node = neighbor_per_node
        self.process_time = process_time
        self.sending_time = sending_time
        self.first_node = None
        self.routing_mode = routing_mode  # parallel or serial
        self.all_nodes = {}

    def create_network(self):
        self.all_nodes = {}
        self.all_nodes[0] = Node.Node(0, self.process_time, self.sending_time)
        for i in range(self.nodes_number + 1):
            if i == 0:  # first node init separately
                continue
            self.all_nodes[i] = Node.Node(i, self.process_time, self.sending_time)
        count = 0
        # connecting the neighbor
        for i in range(self.nodes_number + 1):
            while len(self.all_nodes[i].neighbors) != self.neighbor_per_node:
                count += 1
                if count > self.neighbor_per_node * self.nodes_number * 100:
                    self.all_nodes[i].add_neighbor(self.all_nodes[i])
                    continue
                neighbor_id = random.randint(0, self.nodes_number)
                if neighbor_id == i:
                    continue
                if len(self.all_nodes[neighbor_id].neighbors) == self.neighbor_per_node:
                    continue
                neighbor_ids = [lambda x: x.id for x in self.all_nodes[i].neighbors]
                if neighbor_id in neighbor_ids:
                    continue
                self.all_nodes[neighbor_id].add_neighbor(self.all_nodes[i])
                self.all_nodes[i].add_neighbor(self.all_nodes[neighbor_id])

    def print_map(self):
        print(f"Printing all neighbors in the network:")
        for node in self.all_nodes:
            print(f"Node {node}: Neighbors: {self.all_nodes[node].print_neighbors()}")
