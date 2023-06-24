import network as Network
import create_graphs

def main():
    net1 = Network.Network(nodes_number=100,
                           neighbor_per_node=4,
                           process_time=6,
                           sending_time=2,
                           routing_mode='PARALLEL')
    net2 = Network.Network(nodes_number=100,
                           neighbor_per_node=4,
                           process_time=6,
                           sending_time=2,
                           routing_mode='SERIAL')
    net3 = Network.Network(nodes_number=8000,
                           neighbor_per_node=4,
                           process_time=6,
                           sending_time=2,
                           routing_mode='SERIAL',
                           propagation_delay=2)
    net1.create_network()
    net2.create_network()
    print("Net1:")
    net1.print_map()
    print("Net2:")
    net2.print_map()
    # create_graphs.create_graph_neighbors(net1, 'Neighbors_net1')
    # create_graphs.create_graph_neighbors(net1, 'Neighbors_net2')
    # net2.get_all_clusters_wrap()
    # net2.propagate_block_serial_wrap()
    # create_graphs.create_graph_number_of_node_per_time(net2, 'number_of_node_per_time_net2')

    net3.create_network()
    # net3.propagate_block_serial_wrap()
    # create_graphs.create_graph_number_of_node_per_time(net3, 'number_of_node_per_time_net3')
    #
    # net2.propagate_block_parallel_wrap()
    # create_graphs.create_graph_number_of_node_per_time(net2, 'number_of_node_per_time_net2_parallel')

    net3.propagate_block_serial_wrap()
    x_serial, y_serial = net3.get_number_of_nodes_per_time()
    net3.propagate_block_parallel_wrap()
    x_par, y_par = net3.get_number_of_nodes_per_time()
    create_graphs.create_two_graph("# propagated nodes by time", x_serial, y_serial, x_par, y_par, net3.nodes_number)
    # create_graphs.create_graph_number_of_node_per_time(net3, 'number_of_node_per_time_net3_parallel')


    print(0)


if __name__ == "__main__":
    main()
