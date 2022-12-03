import sqlite3

class Database:
    def add_highscore (id_num,nombre,puntuacion):
        with sqlite3.connect("db_highscore.db") as database:
            database.execute("insert into highscore (ID,nombre,puntuacion) values (?,?,?)", (id_num,nombre,puntuacion))
            database.commit()
            
    def update_highscore(nombre,score):
        with sqlite3.connect("db_highscore.db") as database:
            update = database.execute("UPDATE highscore SET puntuacion = '{0}' WHERE nombre=?".format(score),(nombre,))
            players = update.fetchall()
            for player in players:
                print(player)
            
    def delete_highscore(nombre):
        with sqlite3.connect("db_highscore.db") as database:
            update = database.execute("DELETE FROM highscore WHERE nombre=?",(nombre,))
            players = update.fetchall()
            for player in players:
                print(player)
    
    def check_registered_highscore (nombre):
        with sqlite3.connect("db_highscore.db") as database:
            display = database.execute("SELECT * FROM highscore")
            for player in display:
                if (player[1] == nombre):
                    return True
                else:
                    return False
                
    def compare_highscore (nombre,score):
        with sqlite3.connect("db_highscore.db") as database:
            display = database.execute("SELECT * FROM highscore WHERE nombre=?",(nombre,))
            for player in display:
                if (player[2] < score):
                    return True
                else:
                    return False
            
    def display_highscore (nombre):
        with sqlite3.connect("db_highscore.db") as database:
            display = database.execute("SELECT * FROM highscore WHERE nombre=?",(nombre,))
            for player in display:
                return player

    def display_all_highscore ():
        with sqlite3.connect("db_highscore.db") as database:
            highscore_list = []
            display = database.execute("SELECT ID,nombre,puntuacion FROM highscore ORDER BY puntuacion DESC LIMIT 5;")
            for player in display:
                highscore_list.append(player)
            return highscore_list