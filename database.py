import sqlite3

class Database:
    """
    Base de datos para la tabla de puntuaciones.
    """
    
    def add_highscore (nombre:str,score:int) -> None:
        """
        Agrega el nombre y puntuación de un nuevo jugador a la base de datos.
        
        No retorna nada.
        
        ----------
        nombre : str
            nombre del jugador
        puntuacion : int
            puntuación del jugador
        """
        
        with sqlite3.connect("db_highscore.db") as database:
            database.execute("INSERT into highscore (nombre,puntuacion) values (?,?)", (nombre,score))
            database.commit()
            
    def update_highscore(nombre:str,score:int) -> None:
        """
        Actualiza la puntuación de un jugador ya registrado en la base de datos.
        
        No retorna nada.
        
        ----------
        nombre : str
            nombre del jugador registrado
        puntuacion : int
            puntuación del jugador
        """
        
        with sqlite3.connect("db_highscore.db") as database:
            update = database.execute("UPDATE highscore SET puntuacion = '{0}' WHERE nombre=?".format(score),(nombre,))
            players = update.fetchall()
            for player in players:
                print(player)
            
    def delete_highscore(nombre:str) -> None:
        """
        Borra la entrada en la base de datos correspondiente al nombre recibido.
        
        No retorna nada.
        
        ----------
        nombre : str
            nombre del jugador a borrar
        """
        
        with sqlite3.connect("db_highscore.db") as database:
            update = database.execute("DELETE FROM highscore WHERE nombre=?",(nombre,))
            players = update.fetchall()
            for player in players:
                print(player)
    
    def check_registered_highscore (nombre:str) -> bool:
        """
        Comprueba si el nombre recibido ya existe en la base de datos.
        
        Si es el caso, retorna True.
        
        Si no es el caso, retorna False.
        
        ----------
        nombre : str
            nombre del jugador
        """
        
        with sqlite3.connect("db_highscore.db") as database:
            display = database.execute("SELECT * FROM highscore")
            for player in display:
                if (player[1] == nombre):
                    return True
                else:
                    return False
                
    def compare_highscore (nombre:str,score:int) -> bool:
        """
        Comprueba si la la puntuación recibida es mayor que la puntuación registrada del jugador indicado.
        
        Si es el caso, retorna True.
        
        Si no es el caso, retorna False.
        
        ----------
        nombre : str
            nombre del jugador registrado
        puntuacion : int
            nueva puntuación del jugador
        """
        
        with sqlite3.connect("db_highscore.db") as database:
            display = database.execute("SELECT * FROM highscore WHERE nombre=?",(nombre,))
            for player in display:
                if (player[2] < score):
                    return True
                else:
                    return False
            
    def display_highscore (nombre:str):
        """
        Busca en la base de datos la entrada correspondiente al nombre recibido.
        
        Retorna los datos de la entrada.
        
        ----------
        nombre : str
            nombre del jugador a buscar
        """
        
        with sqlite3.connect("db_highscore.db") as database:
            display = database.execute("SELECT * FROM highscore WHERE nombre=?",(nombre,))
            for player in display:
                return player

    def display_all_highscore ():
        """
        Comprueba si la la puntuación recibida es mayor que la puntuación registrada del jugador indicado.
        
        Si es el caso, retorna True.
        
        Si no es el caso, retorna False.
        
        ----------
        nombre : str
            nombre del jugador registrado
        puntuacion : int
            nueva puntuación del jugador
        """
        
        with sqlite3.connect("db_highscore.db") as database:
            highscore_list = []
            display = database.execute("SELECT ID,nombre,puntuacion FROM highscore ORDER BY puntuacion DESC LIMIT 5;")
            for player in display:
                highscore_list.append(player)
            return highscore_list
        
        
print(type(Database.display_highscore("AAAA")))