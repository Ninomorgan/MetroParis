from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()

        # 1) cosa da fare istanziare il grado con nodi con fermate visibile solo al modello
        self._grafo=nx.DiGraph() #grafo semplice, orientato , non pesato

        #2)devo associare a un id fermata mi returna
        self._idMapFermate = {}
        for f in self._fermate:
            self._idMapFermate[f.id_fermata] = f

    def buildGraph(self): #questo viene chiamato all'inizio, prima lo svuotiaamo,

        #devo mettere i dati qua dentro
        #1)svuotiamolo
        self._grafo.clear()

        #2) tutte le fermate sono contenute dalla query nel dao SELECt * form fermata
        self._grafo.add_nodes_from(self._fermate)

        #3) agigugniamo i nodi e creiamo una funzione
        self.addEdges3()

    #metodi che mi permettono di aspere quanti noid e archi ho
    def get_numNodi(self):
        return len(self._grafo.nodes)

    def get_numArchi(self):
        return len(self._grafo.edges)

    def addEdges(self):
        #creaimo gli archi se c'è una connesione
        for u in self._fermate:
            for v in self._fermate:
                if DAO.hasconn(u,v): # se c'è una connessione tra le fermate è true --> andiamo nel dao e la creiamo
                    self._grafo.add_edge(u, v) #aggiugnaimo

    #COSI MEGLIO
    def addEdges2(self):
        for u in self._fermate:
            #per ogni nodo prendo i vicini (tutti quelli con cui è connesso e li metto nell edge
           # for v in DAO.getVicini(u): non avrrmo direttamente v
            #    self._grafo.add_edge(u, v)
            for conn in DAO.getVicini(u):
                v = self._idMapFermate[conn.id_stazA] #prediamo le stazioni di arrivo
                self._grafo.add_edge(u, v)

    #otteniamo direttamente dlle connessioni -- TUTTO QUESTO ESSENZIALE PER 18
    def addEdges3(self):
        alledges= DAO.getAllEdges()
        for conn in alledges:
            u=self._idMapFermate[conn.id_stazP]
            v=self._idMapFermate[conn.id_stazA]
            self._grafo.add_edge(u, v)

    #4) aggiungiamo i metodi per le visite del grafo
    def getBFSNodesFrom(self, source): #source rappresenta il nodo di partenza
        archi=nx.bfs_edges(self._grafo,source) #passiamo il grafo e il source --> resituisce liste di tuple
        nodiBFS= []
        for u,v in archi:
            #ci chiedono tutti i nodi che possiamo esplorare da nodo source a nodo target
            nodiBFS.append(v) #perchè quelli in partnza già li prndiamo
        return nodiBFS

    def getDFSNodesFrom(self, source):
        archi = nx.dfs_edges(self._grafo, source)  # passiamo il grafo e il source --> resituisce liste di tuple
        nodiDFS = []
        for u, v in archi:
            # ci chiedono tutti i nodi che possiamo esplorare da nodo source a nodo target
            nodiDFS.append(v)  # perchè quelli in partnza già li prndiamo
        return nodiDFS

    #metodo con tree --> uguali risultati --> il primo da un archi il seconod direttamente il grafo
    def getBFSNodesFromTree(self, source): #source rappresenta il nodo di partenza
        tree=nx.bfs_tree(self._grafo,source) #passiamo il grafo e il source --> resituisce liste di tuple
        archi = list(tree.edges)
        nodiBFS = list(tree.nodes) #contiene anche il source
        return nodiBFS


    def getDFSNodesFromTree(self, source): #source rappresenta il nodo di partenza
        tree=nx.dfs_tree(self._grafo,source) #passiamo il grafo e il source --> resituisce liste di tuple
        archi = list(tree.edges)
        nodiDFS = list(tree.nodes) #contiene anche il source
        return nodiDFS


    @property
    def fermate(self):
        return self._fermate

    @property
    def grafo(self):
        return self._grafo