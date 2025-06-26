import pickle

def get_triples_about(entity, graph_path="D:\\Data Science\\knowledge-graph-chatbot\\kg\\graph.gpickle"):
    with open(graph_path, "rb") as f:
        G = pickle.load(f)

    triples = []
    if entity in G:
        for neighbor in G.successors(entity):
            relation = G[entity][neighbor]["relation"]
            triples.append((entity, relation, neighbor))
    return triples