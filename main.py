import networkx as nx
import matplotlib.pyplot as plt


class Network:
    def __init__(self):
        # Initialize the graph
        self.graph = nx.Graph()
        self.create_network()

    def create_network(self):
        # Add nodes
        nodes = [
            "Router", "Switch1", "Switch2",
            "Faculty", "Admin", "Staff",
            "Students", "Lab1", "Lab2",
            "Library", "Auditorium", "IT",
            "Server1", "Server2"
        ]
        self.graph.add_nodes_from(nodes)

        # Add weighted edges
        edges = [
            ("Router", "Switch1", 5),
            ("Router", "Switch2", 8),
            ("Switch1", "Faculty", 3),
            ("Switch1", "Admin", 4),
            ("Switch1", "Staff", 2),
            ("Switch1", "IT", 5),
            ("Switch1", "Library", 7),
            ("Switch2", "Students", 6),
            ("Switch2", "Lab1", 4),
            ("Switch2", "Lab2", 4),
            ("Switch2", "Auditorium", 6),
            ("Switch2", "Server1", 8),
            ("Switch2", "Server2", 10),
            ("Switch1", "Switch2", 12)  # Cross-link
        ]
        self.graph.add_weighted_edges_from(edges)

    def display_network(self):
        # Visualize the graph
        pos = nx.spring_layout(self.graph)  # Layout for clear visualization
        plt.figure(figsize=(12, 10))
        nx.draw(
            self.graph, pos, with_labels=True,
            node_color="lightblue", edge_color="gray",
            node_size=3000, font_size=10
        )

        # Draw edge weights
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)

        plt.title("Enhanced SCES School Network Topology")
        plt.show()

    def find_shortest_path(self, source, target):
        try:
            path = nx.shortest_path(self.graph, source=source, target=target, weight='weight')
            weight = nx.shortest_path_length(self.graph, source=source, target=target, weight='weight')
            return f"Shortest path from {source} to {target}: {path} with total weight {weight}"
        except nx.NetworkXNoPath:
            return f"No path exists between {source} and {target}."

    def identify_critical_nodes(self):
        centrality = nx.betweenness_centrality(self.graph, weight='weight')
        critical_node = max(centrality, key=centrality.get)
        return f"Critical Node: {critical_node}, Centrality: {centrality[critical_node]:.4f}"

    def simulate_failures(self, nodes_to_remove):
        modified_graph = self.graph.copy()
        for node in nodes_to_remove:
            if node in modified_graph:
                modified_graph.remove_node(node)
        is_connected = nx.is_connected(modified_graph)
        return modified_graph, is_connected


# Interactive User Interface
def main():
    network = Network()
    while True:
        # Display the network at the start
        print("\nDisplaying Enhanced SCES School Network...")
        network.display_network()

        # Present menu to user
        print("\nChoose an option:")
        print("1. Find Shortest Path")
        print("2. Identify Critical Nodes")
        print("3. Simulate Node Failures")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            source = input("Enter source node: ")
            target = input("Enter target node: ")
            print(network.find_shortest_path(source, target))

        elif choice == "2":
            print(network.identify_critical_nodes())

        elif choice == "3":
            nodes = input("Enter nodes to remove (comma-separated): ").split(",")
            nodes = [node.strip() for node in nodes]
            modified_graph, is_connected = network.simulate_failures(nodes)

            # Display results
            print(f"Is the network still connected after removing {nodes}? {is_connected}")
            print("\nUpdated Network Topology:")
            pos = nx.spring_layout(modified_graph)  # Layout for clear visualization
            plt.figure(figsize=(12, 10))
            nx.draw(
                modified_graph, pos, with_labels=True,
                node_color="salmon", edge_color="gray",
                node_size=3000, font_size=10
            )
            edge_labels = nx.get_edge_attributes(modified_graph, 'weight')
            nx.draw_networkx_edge_labels(modified_graph, pos, edge_labels=edge_labels)
            plt.title(f"SCES Network After Removing {nodes}")
            plt.show()

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
