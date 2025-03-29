from src.models.nav_graph import NavGraph

def main():
    print("\nFleet Management System: Graph Loading Test\n")
    
    # Choose which nav_graph to load
    file_path = input("Enter the nav_graph file path (e.g., data/nav_graph.json): ")
    
    # Load and display graph info
    nav_graph = NavGraph(file_path)
    nav_graph.display_graph_summary()
    
    # Check vertex information
    sample_index = int(input("Enter a vertex index to view details (e.g., 0, 1, 2...): "))
    vertex_info = nav_graph.get_vertex_info(sample_index)
    
    if vertex_info:
        print(f"\nVertex {sample_index} Info: {vertex_info}")
    else:
        print(f"Vertex {sample_index} not found.")

if __name__ == "__main__":
    main()
