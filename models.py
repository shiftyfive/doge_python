import sqlite3

def drop_table():
    with sqlite3.connect('doges.db') as connection:
        c = connection.cursor()
        c.execute("""DROP TABLE IF EXISTS doggos;""")
        c.execute("""DROP TABLE IF EXISTS humans;""")
    return True

def create_db():
    with sqlite3.connect('doges.db') as connection:
        c = connection.cursor()
        table = """CREATE TABLE doggos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            breed TEXT NOT NULL,
            rating INTEGER NOT NULL
        );
        """
        c.execute(table)
    return True

def createOwners():
    with sqlite3.connect('doges.db') as connection:
        c = connection.cursor()
        table = """CREATE TABLE humans(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            picture_url TEXT,
            doggoid INTEGER,
            FOREIGN KEY(doggoid) REFERENCES doggos(id)
        );
        """
        c.execute(table)
    return True

if __name__ == '__main__':
    drop_table()
    create_db()
    createOwners()
