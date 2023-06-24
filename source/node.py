class Node:
    def __init__(self, id, process_time, sending_time):
        self.id = id
        self.process_time = process_time
        self.neighbors = []
        self.sending_time = sending_time
        self.current_blocks = {}

    def get_all_neighbors_ids(self, ids, timer):
        if timer > 5:
            return
        for child in self.neighbors:
            if child.id not in ids:
                ids.append(child.id)
            child.get_all_neighbors_ids(ids, timer + 1)

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def check_if_block_exist(self, block_id):
        return bool(self.current_blocks.get(block_id, None))

    def send_block(self, neighbor, block_id, is_parallel):
        # print(f"sending block {self.id} -> {neighbor.id}")
        sending_time = self.sending_time
        if is_parallel:
            sending_time *= len(neighbor.neighbors)
        total_time = sending_time
        #INV + get_data
        # if neighbor.check_if_block_exist(block_id):
        #     print(f"block id: {block_id} already exists at {neighbor.id}")
        #     return total_time
        # Transaction
        # total_time += sending_time
        neighbor.current_blocks[block_id] = block_id
        return total_time

    def print_neighbors(self):
        return_str = ''
        for node in self.neighbors:
            return_str += f' {node.id}'
        return return_str

