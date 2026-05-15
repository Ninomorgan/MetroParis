from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.fermata import Fermata



class DAO():

    @staticmethod
    def getAllFermate(): #prende tutte le fermate
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM fermata"
        cursor.execute(query)

        for row in cursor:
            result.append(Fermata(**row))
        cursor.close()
        conn.close()
        return result

#creaiamo la nuova funzione --> facciamo copia e incolla di quella sopra
    @staticmethod
    def hasconn(u:Fermata,v:Fermata):  # prende tutte le fermate
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = ("select * from connessione c "
                 "where c.id_stazP = %s and c.id_stazA = %s ")
        cursor.execute(query,(u.id_fermata,v.id_fermata)) #aggiungiamo u.idfermata e v.idferata confrono el cose

        for row in cursor: #
            #result.append(Fermata(**row)) #vogliamo solo vedere se ci sono o no quindi a noi
            result.append(row)
        cursor.close()
        conn.close()
        return len(result) > 0 #mi dirà se true o false

    @staticmethod
    def getVicini(u):  # prende tutte le fermate
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = ("select * from connessione c "
                 "where c.id_stazP = %s")
        cursor.execute(query, (u.id_fermata,))

        #aggiungo in model una class connesisone
        for row in cursor:
            result.append(Connessione(**row)) #importiamo connessione e tutti i suoi darti
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges():  # prende tutte le fermate
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM connessione c "
        cursor.execute(query)

        for row in cursor:
            result.append(Connessione(**row))
        cursor.close()
        conn.close()
        return result