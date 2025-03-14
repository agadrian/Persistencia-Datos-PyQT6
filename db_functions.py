import sqlite3
import pyrebase
import os

# Configuracion Firebase
firebase_config = {
    "apiKey": "AIzaSyCQy1F8kgeu14Ue9hIZvmt2BFrsbKuNT8Y",
    "authDomain": "proyecto-pyqt.firebaseapp.com",
    "databaseURL": "",
    "projectId": "proyecto-pyqt",
    "storageBucket": "proyecto-pyqt.firebasestorage.app",
    "messagingSenderId": "456522722623",
    "appId": "1:456522722623:web:1c718668b012138f29778a",
    "measurementId": "G-TXQWM1E404"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()


# Diccionario de errores de Fireabse
FIREBASE_ERRORS = {
    "EMAIL_NOT_FOUND": "Este correo no está registrado.",
    "INVALID_PASSWORD": "La contraseña ingresada es incorrecta.",
    "MISSING_PASSWORD": "Contraseña requerida.",
    "USER_DISABLED": "Esta cuenta ha sido deshabilitada.",
    "INVALID_EMAIL": "El correo ingresado no es válido.",
    "INVALID_LOGIN_CREDENTIALS": "Credenciales incorrectas.",
    "TOO_MANY_ATTEMPTS_TRY_LATER": "Has intentado demasiadas veces. Intenta más tarde.",
    "WEAK_PASSWORD": "Contraseña demasiado débil.",
    "EMAIL_EXISTS": "El correo ingresado ya está registrado.",
}


# Obtener conexion de la base de datos
def get_db_connection():
    try:
        from utils import resource_path
        db_path = resource_path("database.db")
        conn = sqlite3.connect(db_path)  
        cursor = conn.cursor() 
        return conn, cursor 
    except sqlite3.Error as e:
        print(f"Error de conexión con la base de datos: {e}")
        return None, None

# Cerrar la conexion de la base de datos
def close_db_connection(conn):
    try:
        if conn:
            conn.close() 
    except sqlite3.Error as e:
        print(f"Error al cerrar la conexión: {e}")

