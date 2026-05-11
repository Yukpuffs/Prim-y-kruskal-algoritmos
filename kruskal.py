import networkx as nx
import matplotlib.pyplot as plt

nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'Q']

aristas = [
    (2, 'D', 'E'),
    (6, 'D', 'B'),
    (9, 'E', 'B'),
    (7, 'B', 'A'),
    (4, 'B', 'C'),
    (5, 'A', 'C'),
    (3, 'C', 'E'),
    (6, 'C', 'Q'),
    (10, 'F', 'Q'),
    (11, 'E', 'F')
]

class Acueducto_k:
    def __init__(self, nodos):
        self.padre = {n: n for n in nodos}
        self.rango = {n: 0 for n in nodos}

    def buscar(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.buscar(self.padre[x])
        return self.padre[x]
    
    def unir(self, x, y):
        rx, ry = self.buscar(x), self.buscar(y)
        if rx == ry:
            return False
        if self.rango[rx] < self.rango[ry]:
            rx, ry = ry, rx
        self.padre[ry] = rx

        if self.rango[rx] == self.rango[ry]:
            self.rango[rx] += 1
        return True

def Kruskal(nodos, aristas):

    ordenado = sorted(aristas)
    conexion = Acueducto_k(nodos)
    mst = []
    total = 0

    for peso, u, v in ordenado:
        if conexion.unir(u, v):
            mst.append((u, v, peso))
            total += peso
            if len(mst) == len(nodos) - 1:
                break
    return mst, total

mst, costo = Kruskal(nodos, aristas)
print(f"Costo total MST: {costo}")
for u, v, w in mst:
    print(f"  {u} {w} {v}")


G = nx.Graph()

for u, v, peso in mst:
    G.add_edge(u, v, weight=peso)

pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color='#D3968C',
    node_size=3000,
    font_size=12,
    font_weight='bold'
)

labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=labels
)

plt.title("Árbol de Expansión Mínima - Kruskal")

plt.show()