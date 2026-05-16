import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

#3) colleghiamo il nostro grafo al controller
    def handleCreaGrafo(self,e):
        #crea il grafo chiamanto buildgraph
        self._model.buildGraph()

        #aggiungiamo anche i metodi

        #svuotiamo finestra
        self._view.lst_result.controls.clear()
        #appendimao nella lista
        self._view.lst_result.controls.append(ft.Text("Grafo creato corratmente"))
        self._view.lst_result.controls.append(ft.Text(f"il Grafo creato ha {self._model.get_numNodi()} nodi"))
        self._view.lst_result.controls.append(ft.Text(f"il Grafo creato ha {self._model.get_numArchi()} archi"))
        self._view.update_page()

    def handleCercaRaggiungibili(self,e):
        #dfs / bfs edges (archi attraversati da algoritmo)
        # dfs/ bfs tree (da un grafo)

        #riempiamo il metodo dopo aver creato nel model i metodi per torvare gli archi dal source

        if self._fermataPartenza is None:
            self._view.lst_result.controls.clear()
            self._view.lst_result.controls.append(ft.Text("Attenzione non hai selezionato una stazione di partenza", color="red"))
            self._view.update_page()

        #ha scelto una partenza --> ciediamo al modello di dirci le stazooni raggiugnibili

        nodes = self._model.getBFSNodesFrom(self._fermataPartenza)
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text(f"DI seugito le stazioni raggiungibili da {self._fermataPartenza}"))
        for n in nodes:
            self._view.lst_result.controls.append(ft.Text(n))
        self._view.update_page()



    def loadFermate(self, dd: ft.Dropdown()):
        fermate = self._model.fermate

        if dd.label == "Stazione di Partenza":
            for f in fermate:
                dd.options.append(ft.dropdown.Option(text=f.nome,
                                                     data=f, #elemento fermata
                                                     on_click=self.read_DD_Partenza)) #associamo un metodo
        elif dd.label == "Stazione di Arrivo":
            for f in fermate:
                dd.options.append(ft.dropdown.Option(text=f.nome,
                                                     data=f,
                                                     on_click=self.read_DD_Arrivo))

    def read_DD_Partenza(self,e):
        print("read_DD_Partenza called ")
        if e.control.data is None:
            self._fermataPartenza = None
        else:
            self._fermataPartenza = e.control.data

    def read_DD_Arrivo(self,e):
        print("read_DD_Arrivo called ")
        if e.control.data is None:
            self._fermataArrivo = None
        else:
            self._fermataArrivo = e.control.data
