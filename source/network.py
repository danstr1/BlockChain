import node as Node
import random
from collections import defaultdict

class Network:
    def __init__(self, nodes_number, neighbor_per_node, process_time, sending_time, routing_mode, propagation_delay=0):
        self.nodes_number = nodes_number
        self.neighbor_per_node = neighbor_per_node
        self.process_time = process_time
        self.sending_time = sending_time
        self.first_node = None
        self.routing_mode = routing_mode  # parallel or serial
        self.all_nodes = {}
        self.propagate_node_by_time = defaultdict(list)  # time (int) -> list of nodes get the block
        self.current_time = 0
        self.propagation_delay = propagation_delay

    def create_network(self):
        self.all_nodes = {}
        self.all_nodes[0] = Node.Node(0, self.process_time, self.sending_time)
        nodes_number = int(self.nodes_number * 1.1)
        for i in range(nodes_number + 1):
            if i == 0:  # first node init separately
                continue
            self.all_nodes[i] = Node.Node(i, self.process_time, self.sending_time)
        count = 0
        # connecting the neighbor
        for i in range(nodes_number + 1):
            while len(self.all_nodes[i].neighbors) != self.neighbor_per_node:
                count += 1
                if count > self.neighbor_per_node * nodes_number * 100:
                    self.all_nodes[i].add_neighbor(self.all_nodes[i])
                    continue
                neighbor_id = random.randint(0, nodes_number)
                if neighbor_id == i:
                    continue
                if len(self.all_nodes[neighbor_id].neighbors) == self.neighbor_per_node:
                    continue
                neighbor_ids = [lambda x: x.id for x in self.all_nodes[i].neighbors]
                if neighbor_id in neighbor_ids:
                    continue
                self.all_nodes[neighbor_id].add_neighbor(self.all_nodes[i])
                self.all_nodes[i].add_neighbor(self.all_nodes[neighbor_id])

    def get_all_clusters_wrap(self):
        all_ids = []
        all_clusters = []
        node = self.all_nodes[0]
        current_ids = []
        node.get_all_neighbors_ids(current_ids, 0)
        all_clusters.append(current_ids)
        all_ids += current_ids
        while len(all_ids) < self.nodes_number:
            for i in range(self.nodes_number):
                if i not in all_ids:
                    current_ids = []
                    self.all_nodes[i].get_all_neighbors_ids(current_ids, 0)
                    all_clusters.append(current_ids)
                    all_ids += current_ids
                    break
        print(f"all_clusters = \n{all_clusters}")
        print(f"all_ids = \n{all_ids}")

    def fix_propogate_node(self):
        total_till_now = []
        for elem in sorted(self.propagate_node_by_time):
            for node in self.propagate_node_by_time[elem]:
                if node not in total_till_now:
                    total_till_now.append(node)
            for node in total_till_now:
                if node not in self.propagate_node_by_time[elem]:
                    self.propagate_node_by_time[elem].append(node)
        self.propagate_node_by_time = dict(sorted(self.propagate_node_by_time.items(), key=lambda item: item[0]))

    def propagate_block_serial_wrap(self):
        self.propagate_node_by_time = defaultdict(list)
        node = self.all_nodes[0]
        self.propagate_block_serial(node, 0, 0)
        self.fix_propogate_node()

    def propagate_block_parallel_wrap(self):
        self.propagate_node_by_time = defaultdict(list)
        node = self.all_nodes[0]
        self.propagate_block_parallel(node, 0, 0)
        self.fix_propogate_node()

    def get_time_node_inserted(self, node):
        for time in self.propagate_node_by_time:
            for elem in self.propagate_node_by_time[time]:
                if elem.id == node.id:
                    return time
        return 0

    def get_number_of_nodes_per_time(self):
        x = []
        first_time = True
        y = []
        for i in self.propagate_node_by_time:
            # if len(self.propagate_node_by_time[i]) >= 0.7 * len(self.all_nodes) and not first_time:
            #     break
            # elif len(self.propagate_node_by_time[i]) >= 0.7 * len(self.all_nodes):
            #     first_time = False
            x.append(i)
            y.append(len(self.propagate_node_by_time[i]))
        return x, y

    def propagate_block_serial(self, node, current_time, max_depth):
        # all_get_msg = True
        # for i in range(self.nodes_number):
        #     if not self.all_nodes[i].check_if_block_exist(1):
        #         all_get_msg = False
        # if all_get_msg:
        #     return
        if max_depth > 7:
            return
        current_time += node.process_time
        if node not in self.propagate_node_by_time[current_time]:
            self.propagate_node_by_time[current_time].append(node)

        for neighbor in node.neighbors:
            # if (not neighbor.check_if_block_exist(1)) or self.get_time_node_inserted(neighbor) > current_time:
                time_taken = self.propagation_delay + node.send_block(neighbor, 1, False)
                # current_time_taken = current_time + time_taken

                # current_time_for_child = current_time + time_taken
                current_time += time_taken

                # self.propagate_node_by_time[current_time].append(neighbor) if neighbor not in \
                #                       self.propagate_node_by_time[current_time] else None
                self.propagate_block_serial(neighbor, current_time, max_depth + 1)

    def propagate_block_parallel(self, node, current_time, max_depth):
        # all_get_msg = True
        # for i in range(self.nodes_number):
        #     if not self.all_nodes[i].check_if_block_exist(1):
        #         all_get_msg = False
        # if all_get_msg:
        #     return
        if max_depth > 7:
            return
        current_time += node.process_time
        if node not in self.propagate_node_by_time[current_time]:
            self.propagate_node_by_time[current_time].append(node)

        for neighbor in node.neighbors:
            # if (not neighbor.check_if_block_exist(1)) or self.get_time_node_inserted(neighbor) > current_time:
                time_taken = self.propagation_delay + node.send_block(neighbor, 1, True)
                # current_time_taken = current_time + time_taken
                # self.propagate_node_by_time[current_time].append(neighbor) if neighbor not in \
                #                       self.propagate_node_by_time[current_time] else None
                self.propagate_block_parallel(neighbor, current_time + time_taken, max_depth + 1)


    def print_map(self):
        print(f"Printing all neighbors in the network:")
        for node in self.all_nodes:
            print(f"Node {node}: Neighbors: {self.all_nodes[node].print_neighbors()}")
