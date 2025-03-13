from login import *
from register import RegisterWindow
from home import HomeWindow
import sys
from PyQt6.QtCore import Qt, QPoint
from PyQt6 import uic  
from PyQt6.QtGui import QIcon


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Just Meat App")
        self.setWindowIcon(QIcon("ui/res/logo.png"))
        
        
        # Crear stack para navegar 
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.stack.setSizePolicy(self.sizePolicy())

        


        # Instanciar clases
        self.login_page = LoginWindow(self)
        self.register_page = RegisterWindow(self)
        
        
        # Agregar pages al stack
        self.stack.addWidget(self.login_page)
        self.stack.addWidget(self.register_page)
        
        
        # Predeterminada
        self.stack.setCurrentWidget(self.login_page)
        
    

    def switch_to_register(self):
        self.stack.setCurrentWidget(self.register_page)
        
    
    def switch_to_login(self):
        self.stack.setCurrentWidget(self.login_page)
    
        
    def switch_to_main(self):
        self.close()
        self.mainWindow = HomeWindow()
        self.mainWindow.show()

        #self.stack.setCurrentWidget(HomeWindow())
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.setFixedSize(850, 700)
    window.show()
    app.exec()