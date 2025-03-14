from login import *
from register import RegisterWindow
from home import HomeWindow
import sys
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from PyQt6.QtGui import QIcon
from utils import resource_path


# pyinstaller --name "JustMeatApp" --add-data "database.db;." --add-data "ui/pages;ui/pages" --add-data "ui/dialogs;ui/dialogs" --add-data "ui/res;ui/res" --add-data "dialogs;dialogs" --windowed main.py

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Just Meat App")
        self.setWindowIcon(QIcon(resource_path("ui/res/logo.png")))
        
        
        # Crear stack para navegar 
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.stack.setSizePolicy(self.sizePolicy())

        # Imagen de fondo, login  y register
        bg_path = resource_path("ui/res/bg.png")  # Convierte la ruta para problemas con pyinstaller
        print(bg_path)
        self.stack.setStyleSheet(f"""
            QStackedWidget {{
                background-image: url("{bg_path}");
            }}
        """)

    

        # Instanciar clases
        self.login_page = LoginWindow(self)
        self.register_page = RegisterWindow(self)
        
        
        # Agregar pages al stack
        self.stack.addWidget(self.login_page)
        self.stack.addWidget(self.register_page)
        
        
        # Predeterminada
        self.stack.setCurrentWidget(self.login_page)
        
    
    # Cambio de paginas, al regiser o al login
    def switch_to_register(self):
        self.stack.setCurrentWidget(self.register_page)
        
    
    def switch_to_login(self):
        self.stack.setCurrentWidget(self.login_page)
    
        
    def switch_to_main(self):
        self.close()
        self.mainWindow = HomeWindow()
        self.mainWindow.show()

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.setFixedSize(850, 700)
    window.show()
    app.exec()