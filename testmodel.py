#facciamo le prove del buildgraph
from model.fermata import Fermata
from model.model import Model

model=Model()
model.buildGraph()
#print("Numero nodi:", len(model._grafo.nodes)) #dobbiamo crea una funzione
print("Numero nodi:", (model.get_numNodi()))
print("numero archi", model.get_numArchi())

source= Fermata(2,	"Abbesses",	2.33855	,48.8843) #copiato da database

nodiBFS= model.getBFSNodesFromEdges(source)
nodiDFS= model.getDFSNodesFromEdges(source)

#stampiamo archi con peso 2
print ("Archi con peso 2")
archi= model.getArchiWPeso2()
for a in archi:
    print(a[0],a[1], a["weight"])