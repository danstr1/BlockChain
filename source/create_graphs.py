import matplotlib.pyplot as plt

def create_graph_neighbors(network, file_name):
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(30,10))
    x = []
    for i in range(network.nodes_number + 1):
        for a in range(network.neighbor_per_node):
            x.append(i)
    y = []
    for node in network.all_nodes:
        neighbors = network.all_nodes[node].neighbors
        for neighbor in neighbors:
            y.append(neighbor.id)
    # Plot the data
    ax.scatter(x, y)

    # Add labels and title
    ax.set_xlabel('Node id')
    ax.set_ylabel('Neighbors IDs')
    ax.set_title('Neighbors Graph')

    plt.savefig(f'../graphs/{file_name}.png')

    # Display the plot
    plt.show()
