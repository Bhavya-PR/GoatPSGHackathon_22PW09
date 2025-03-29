import json
import networkx as nx

class NavGraph:
    def __init__(self, file_path=None):
        self.graph = nx.Graph()
        self.vertices = []
        self.lanes = []
        
        if file_path:
            self.load_graph(file_path)

    def load_graph(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                level_data = data.get('levels', {}).get('level1', {})

                self.vertices = level_data.get('vertices', [])
                self.lanes = level_data.get('lanes', [])

                if not self.vertices or not self.lanes:
                    print("❗ No vertices or lanes found. Please check the file.")
                    return

                self.build_graph()
                print(f"✅ Successfully loaded graph from {file_path}")
        except Exception as e:
            print(f"❗ Error loading graph: {e}")

    def build_graph(self):
        for i, (x, y, attrs) in enumerate(self.vertices):
            if not attrs.get('name'):
                attrs['name'] = f"Unnamed_V{i}"  # Assign a default name if empty
            self.graph.add_node(i, pos=(x, y), **attrs)
            print(f"Added Vertex {i}: {attrs['name']} at ({x}, {y})")

        for lane in self.lanes:
            start, end = lane[0], lane[1]
            self.graph.add_edge(start, end)
            print(f"Connected Vertex {start} ↔ Vertex {end}")

    def display_graph_summary(self):
        print(f"\nGraph Summary:")
        print(f"🔎 Vertices: {len(self.graph.nodes)}")
        print(f"🔗 Lanes: {len(self.graph.edges)}")

    def get_vertex_info(self, index):
        if index in self.graph.nodes:
            return self.graph.nodes[index]
        return None
