# Prim algorith with python
import heapq # Priority queue 
import matplotlib.pyplot as plt
import networkx as nx

Barrios = [ # Graph with neighborhoods and costs 
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

class Acueducto:

    def __init__(self, Barrios):
        self.Barrios = Barrios
        self.mst = []
        self.total = 0

    def contruccion(self):
        ady = {nodo: [] for costo, Bar1, Bar2 in self.Barrios
            for nodo in [Bar1, Bar2]
        }
            
        for costo, Bar1, Bar2 in Barrios:
            ady[Bar1].append((costo,Bar2))
            ady[Bar2].append((costo,Bar1))

        visitados= set()
        cola = [(0, 'D', 'D')]

        while cola:
            costo, origen, destino = heapq.heappop(cola)

            if destino in visitados:
                continue 

            visitados.add(destino)
            self.total += costo

            if origen != destino:
                self.mst.append((origen, destino, costo))

            for wgt, vec in ady[destino]:
                if vec not in visitados: 
                    heapq.heappush(cola, (wgt, destino, vec))

print("Red de acueducto")

red = Acueducto(Barrios)
red.contruccion()

for a,b,c in red.mst:
    print(f" {a} {c} {b}")

print(f"Total de red de acueducto: {red.total} metros ")

# Graph with network nx

G = nx.Graph()

for origen, destino, costo in red.mst:
    G.add_edge(origen, destino, weight=costo)


pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels = True)

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

plt.show()