import networkx as nx
import matplotlib.pyplot as plt


class Network:
    def __init__(self):
        # Initialize the graph
        self.graph = nx.Graph()
        self.create_network()

    def create_network(self):
        """
                Create the network topology by adding nodes and weighted edges.
        """
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
        """
                Visualize the network topology using Matplotlib.
        """
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
        """
                Find the shortest path between two nodes in the network.

                Parameters:
                source (str): The source node.
                target (str): The target node.

                Returns:
                str: A message with the shortest path and its total weight, or an error message.
        """
        try:
            if source not in self.graph or target not in self.graph:
                return f"Error: One or both nodes '{source}' and '{target}' do not exist in the network."

            path = nx.shortest_path(self.graph, source=source, target=target, weight='weight')
            weight = nx.shortest_path_length(self.graph, source=source, target=target, weight='weight')
            return f"Shortest path from {source} to {target}: {path} with total weight {weight}"
        except nx.NetworkXNoPath:
            return f"No path exists between {source} and {target}."
        except Exception as e:
            return f"An error occurred: {e}"


# Interactive User Interface
def main():
    network = Network()
    while True:
        try:
            # Display the network at the start
            print("\nDisplaying Enhanced SCES School Network...")
            network.display_network()

            # Present menu to user
            print("\nChoose an option:")
            print("1. Find Shortest Path")
            print("2. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                source = input("Enter source node: ")
                target = input("Enter target node: ")
                print(network.find_shortest_path(source, target))

            elif choice == "2":
                print("Exiting the program. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
