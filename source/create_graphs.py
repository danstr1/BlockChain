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


def create_two_graph(title, x_serial, y_serial, x_par, y_par, top, y_title, x_title):
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(x_serial, y_serial, linestyle='--', marker='.')
    ax.plot(x_par, y_par, linestyle='--', marker='o')
    if top:
        plt.ylim(top=top)
    plt.grid(visible=True)
    # Add labels and title
    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)
    ax.set_title(title)
    ax.legend(['Serial propagation', 'Parallel propagation'])

    plt.savefig(f'../graphs/{title}.png')

    # Display the plot
    plt.show()


def create_graph_number_of_node_per_time(network, file_name):
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(15,5))
    x = []
    first_time = True
    y = []
    for i in network.propagate_node_by_time:
        if len(network.propagate_node_by_time[i]) >= 0.7*len(network.all_nodes) and not first_time:
            break
        elif len(network.propagate_node_by_time[i]) >= 0.7*len(network.all_nodes):
            first_time = False
        x.append(i)
        y.append(len(network.propagate_node_by_time[i]))

    # Plot the data
    ax.plot(x, y)

    # Add labels and title
    ax.set_xlabel('Time')
    ax.set_ylabel('Number of node get block')
    ax.set_title(file_name)

    plt.savefig(f'../graphs/{file_name}.png')

    # Display the plot
    plt.show()
    print(0)