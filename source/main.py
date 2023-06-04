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
    net1.create_network()
    net2.create_network()
    print("Net1:")
    net1.print_map()
    print("Net2:")
    net2.print_map()
    create_graphs.create_graph_neighbors(net1, 'Neighbors_net1')
    create_graphs.create_graph_neighbors(net1, 'Neighbors_net2')


if __name__ == "__main__":
    main()
