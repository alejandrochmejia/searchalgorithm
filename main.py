import networkx as nx
import matplotlib.pyplot as plt
import maxpend as mx
import simple
import os

grafo = nx.Graph() #Creación del Grafo

edges = [
    ("A", "D", 1),
    ("A", "Q", 3),
    ("A", "G", 2),
    ("D", "B", 3),
    ("D", "J", 4),
    ("Q", "C", 4),
    ("Q", "E", 6),
    ("C", "W", 8),
    ("C", "P", 4),
    ("E", "Z", float('inf')),
    ("E", "F", 6),
    ("J", "H", 4),
    ("J", "K", 5),
    ("K", "L", float('inf')),
]


grafo.add_weighted_edges_from(edges)

# Definir posiciones manuales para los nodos
pos = {
    "A": (0, 5),
    "D": (-3, 4),
    "Q": (0, 4),
    "G": (3, 4),
    "B": (-4, 3),
    "J": (-2, 3),
    "C": (-1, 3),
    "E": (2, 3),
    "H": (-4, 2),
    "K": (-2, 2),
    "L": (-1, 1),
    "W": (-1, 2),
    "P": (0, 2),
    "Z": (2, 2),
    "F": (3, 2),
}

# Ejecutar el algoritmo con nodo inicial 'A' y nodos finales 'Z' o 'L'
start_node = "A"
end_nodes = {"Z", "L"}
os.system('cls')

print("Escalada Simple:")
path, weight = simple.escalada(grafo, start_node, end_nodes)
print("Camino encontrado:", path)
print("Peso total del camino:", weight)

print("\nEscalada por Máxima Pendiente:")
path, weight = mx.escalada_por_maxima_pendiente(grafo, start_node, end_nodes)
print("Camino encontrado:", path)
print("Peso total del camino:", weight)

nx.draw(grafo, pos, with_labels=True, node_color="lightblue", node_size=1000, font_size=10)
weights = nx.get_edge_attributes(grafo, 'weight')
nx.draw_networkx_edge_labels(grafo, pos, edge_labels=weights)
plt.show()

