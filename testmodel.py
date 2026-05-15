#facciamo le prove del buildgraph

from model.model import Model

model=Model()
model.buildGraph()
#print("Numero nodi:", len(model._grafo.nodes)) #dobbiamo crea una funzione
print("Numero nodi:", (model.get_numNodi()))
print("numero archi", model.get_numArchi())