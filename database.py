import sqlite3 as db


# Fichero para testear funciones sobre la base de datos. ** NO TIENE UTILIDAD EN LA APP **

def create_tables():
    conn = db.connect("database.db")
    cursor = conn.cursor()

    sql_statements = [
        """DROP TABLE IF EXISTS usuarios;""",
        """DROP TABLE IF EXISTS restaurantes;""",
        """DROP TABLE IF EXISTS platos;""",
        """DROP TABLE IF EXISTS pedidos;""",
        """DROP TABLE IF EXISTS detalles_pedido;""",
        """DROP TABLE IF EXISTS repartidores;""",

        """PRAGMA foreign_keys = ON;""",



        """CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT NOT NULL, 
            email TEXT UNIQUE NOT NULL, 
            direccion TEXT, 
            telefono TEXT UNIQUE NULL,
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );""",
        
        """CREATE TABLE IF NOT EXISTS restaurantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT NOT NULL, 
            direccion TEXT NOT NULL, 
            categoria TEXT, 
            telefono TEXT UNIQUE,
            horario TEXT,
            calificacion REAL CHECK (calificacion >= 0 AND calificacion <= 5)
        );""",
        
        """CREATE TABLE IF NOT EXISTS platos (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT NOT NULL, 
            precio REAL NOT NULL CHECK (precio > 0), 
            descripcion TEXT NOT NULL,
            id_restaurante INTEGER NOT NULL, 
            FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id) ON DELETE CASCADE
        );""",
        
        """CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_cliente INTEGER NOT NULL, 
            id_restaurante INTEGER NOT NULL, 
            estado TEXT CHECK (estado IN ('pendiente', 'en preparación', 'en camino', 'entregado')), 
            FOREIGN KEY (id_cliente) REFERENCES usuarios(id) ON DELETE CASCADE,
            FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id) ON DELETE CASCADE
        );""",
        
        """CREATE TABLE IF NOT EXISTS detalles_pedido (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_pedido INTEGER NOT NULL, 
            id_plato INTEGER NOT NULL,
            cantidad INTEGER NOT NULL CHECK (cantidad > 0), 
            FOREIGN KEY (id_pedido) REFERENCES pedidos(id) ON DELETE CASCADE, 
            FOREIGN KEY (id_plato) REFERENCES platos(id) ON DELETE CASCADE
        );""",
        
        """CREATE TABLE IF NOT EXISTS repartidores (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nif TEXT UNIQUE NOT NULL, 
            nombre TEXT NOT NULL, 
            id_pedido_asignado INTEGER, 
            vehiculo TEXT, 
            FOREIGN KEY (id_pedido_asignado) REFERENCES pedidos(id) ON DELETE SET NULL
        );""",
    ]


    for i in sql_statements:
        cursor.execute(i)
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablas = cursor.fetchall()


    print("\nTablas en la BD:")
    for tabla in tablas:
        print(tabla[0])


    conn.commit()
    conn.close()





def ver_usuarios():
    conn = db.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()

    if usuarios:
        for usuario in usuarios:
            print(usuario)
    else:
        print("No hay usuarios en la base de datos.")

    

def exportSQL():
    conn = db.connect("database.db")
    cursor = conn.cursor()
    
    # Abrir el archivo .sql para guardar el volcado
    with open("exportado.sql", "w") as sql_file:
        # Volcar toda la base de datos usando iterdump
        for line in conn.iterdump():
            sql_file.write(f"{line}\n")
    
    print("Exportación completada en el archivo exportado.sql")
    
    conn.close()
    


def vaciar_tablas():
    conn = db.connect("database.db")
    cursor = conn.cursor()

    # Lista de las tablas en la base de datos
    tablas = ['usuarios', 'restaurantes', 'platos', 'pedidos', 'detalles_pedido', 'repartidores']

    # Vaciar cada tabla
    for tabla in tablas:
        cursor.execute(f"DELETE FROM {tabla};")
        print(f"Datos eliminados de la tabla {tabla}.")

    # Confirmar los cambios
    conn.commit()
    conn.close()
    print("Todas las tablas han sido vaciadas.")

if __name__ == "__main__":
    #create_tables()
    #ver_usuarios()
    #exportSQL()
    #insertar_datos_grandes()
    vaciar_tablas()