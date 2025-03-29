import json
import networkx as nx

class NavGraph:
    def __init__(self, file_path):
        self.graph = nx.Graph()
        self.vertices = []
        self.lanes = []
        self.load_graph(file_path)

    def load_graph(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.vertices = data.get('vertices', [])
                self.lanes = data.get('lanes', [])
                
                self.build_graph()
                print(f"✅ Successfully loaded graph from {file_path}")
        except Exception as e:
            print(f"❗ Error loading graph: {e}")

    def build_graph(self):
        # Add vertices to the graph
        for i, (x, y, attrs) in enumerate(self.vertices):
            self.graph.add_node(i, pos=(x, y), **attrs)
        
        # Add lanes (edges) to the graph
        for lane in self.lanes:
            self.graph.add_edge(lane[0], lane[1])

    def get_graph(self):
        return self.graph

    def get_vertex_info(self, index):
        return self.graph.nodes[index] if index in self.graph.nodes else None

    def display_graph_summary(self):
        print(f"Graph has {self.graph.number_of_nodes()} vertices and {self.graph.number_of_edges()} lanes.")
