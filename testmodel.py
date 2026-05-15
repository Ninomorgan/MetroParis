#facciamo le prove del buildgraph
from model.fermata import Fermata
from model.model import Model

model=Model()
model.buildGraph()
#print("Numero nodi:", len(model._grafo.nodes)) #dobbiamo crea una funzione
print("Numero nodi:", (model.get_numNodi()))
print("numero archi", model.get_numArchi())

source= Fermata(2,	"Abbesses",	2.33855	,48.8843) #copiato da database

nodiBFS= model.getBFSNodesFrom(source)
nodiDFS= model.getPDSNodesFrom(source)