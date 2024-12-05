# Basic SCES School Network

This project simulates a basic version of SCES school network using Python, NetworkX, and Matplotlib. It allows users to visualize the network topology and find the shortest path between nodes.

## Features

- Visualize the school network topology
- Find the shortest path between two nodes
- User-friendly interactive interface

## Requirements

- Python 3.6+
- NetworkX
- Matplotlib

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/OCHOLA-EDDYPHIL/NetworkSimulation.git
    ```
    ```sh
    cd (directory)
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1  # On Windows
    source .venv/bin/activate      # On Unix or MacOS
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:
    ```sh
    python main.py
    ```

2. Follow the on-screen instructions to interact with the network.

## Project Structure

- `main.py`: The main script to run the project.
- `requirements.txt`: List of required packages.
- `README.md`: Project documentation.

## Example

```sh
Displaying Enhanced SCES School Network...

Choose an option:
1. Find Shortest Path
2. Exit
Enter your choice: 1
Enter source node: Router
Enter target node: Library
Shortest path from Router to Library: ['Router', 'Switch1', 'Library'] with total weight 12
