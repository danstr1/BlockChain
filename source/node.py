class Node:
    def __init__(self, id, process_time, sending_time):
        self.id = id
        self.process_time = process_time
        self.neighbors = []
        self.sending_time = sending_time
        self.current_blocks = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def check_if_block_exist(self, block_id):
        return self.current_blocks.get(block_id, None) is not None

    def send_block(self, neighbor, block_id):
        total_time = self.sending_time + neighbor.sending_time
        #INV + get_data
        if neighbor.check_if_block_exist(block_id):
            print(f"block id: {block_id} already exists at {neighbor}")
            return total_time
        # Transaction
        total_time += self.sending_time
        total_time += neighbor.process_time
        return total_time

    def print_neighbors(self):
        return_str = ''
        for node in self.neighbors:
            return_str += f' {node.id}'
        return return_str

