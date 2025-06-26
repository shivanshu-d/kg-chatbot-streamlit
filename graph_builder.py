import networkx as nx
import pandas as pd
import pickle

def build_graph(csv_path, output_path):
    df = pd.read_csv(csv_path)
    G = nx.DiGraph()

    for _, row in df.iterrows():
        head, relation, tail = row["Entity1"], row["Relation"], row["Entity2"]
        G.add_node(head)
        G.add_node(tail)
        G.add_edge(head, tail, relation=relation)

    with open(output_path, "wb") as f:
        pickle.dump(G, f)
    print(f"✅ Graph saved at {output_path}")

if __name__ == "__main__":
    build_graph("D:\\Data Science\\knowledge-graph-chatbot\\triples\\extracted_triples.csv", "D:\\Data Science\\knowledge-graph-chatbot\\kg\\graph.gpickle")
