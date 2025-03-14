from dialogs.CreateUserDialog import *
from db_functions import *
from utils import *
from PDFGenerator import PDFGenerator

class usuariosPage(QWidget):
    def __init__(self, home_window):
        super().__init__()
        self.home = home_window

        # Conectar botones
        self.btn_addUser_2 = self.home.btn_addUser_2
        self.btn_addUser_2.clicked.connect(self.open_dialog)
        
        self.btn_exportToPDF = self.home.btn_exportToPDF
        self.btn_exportToPDF.clicked.connect(self.export_pdf)

        self.tabla_users = self.home.tabla_users

        
        # Cargar los usuarios
        self.load_users()

        # Conectar la funcion de search_by_email con el cambio de input del lineEdit
        self.home.lineEdit_search_email.textChanged.connect(self.search_by_email)


        # Espacio de cada columna de la tabla
        self.tabla_users.setColumnWidth(0, 40)
        self.tabla_users.setColumnWidth(1, 140)
        self.tabla_users.setColumnWidth(2, 170)
        self.tabla_users.setColumnWidth(3, 170)
        self.tabla_users.setColumnWidth(4, 120)
        self.tabla_users.setColumnWidth(5, 120)
        self.tabla_users.setColumnWidth(6, 100)
    

    def export_pdf(self):
        pdf = PDFGenerator()
        pdf.generate_table_from_qtwidget(self.tabla_users, title="Informe de datos de la tabla")
        pdf_path = resource_path("Informe_Usuarios.pdf")
        pdf.save(pdf_path)
        QMessageBox.information(self.home, "Éxito", f"PDF Exportado correctamente")


    # Abre el dialogo para crear nuevo user
    def open_dialog(self):
        dialog = UserDialog(self.home)
        dialog.exec()
        self.load_users()        

    
    # Cargar todos los usuarios de la db
    def load_users(self):
        try:
            conn, cursor = get_db_connection()
            if conn is None or cursor is None:
                raise Exception("No se pudo conectar a la base de datos.")

            self.tabla_users.setRowCount(0)

            if not self.tabla_users:
                raise Exception("Error: 'tabla_users' no se encontró en la UI.")
            
            cursor.execute("SELECT id, nombre, email, direccion, telefono, fecha_registro FROM usuarios")
            users = cursor.fetchall()
            print(users) 


            for row_index, row_data in enumerate(users):
                self.tabla_users.insertRow(row_index)
                for col_index, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.tabla_users.setItem(row_index, col_index, item)

                # Crear los dos iconos finales de editar y eliminar (clase ubicada en utils.py)
                edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data, UpdateUserDialog, self.load_users, self.delete_user)

                # Establecer los botones
                self.tabla_users.setCellWidget(row_index, 6, edit_delete_widget)
                self.tabla_users.setRowHeight(row_index, 50)

        except Exception as e:
            QMessageBox.warning(self.home, "Error", f"Error cargando usuarios: {str(e)}")
        finally:
            if conn:
                close_db_connection(conn)


    def search_by_email(self):
        # Limpiar la tabla
        self.tabla_users.setRowCount(0)

        # Input del lineEdit
        input = self.home.lineEdit_search_email.text().strip()

        # Si no hay nada escrito, recargar la tabla con todo los datos
        if not input:
            self.load_users()
            return
            

        # SQL
        try:
            conn, cursor = get_db_connection()
            if conn is None or cursor is None:
                raise Exception("No se pudo conectar a la base de datos.")

            cursor.execute("SELECT * FROM usuarios WHERE email LIKE ? OR nombre LIKE ?", (f"%{input}%", f"%{input}%"))
            users = cursor.fetchall()
        
            # Mostrar filas
            for row_index, row_data in enumerate(users):
                self.tabla_users.insertRow(row_index)
                for col_index, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                    self.tabla_users.setItem(row_index, col_index, item)

                # Crear los dos iconos finales de editar y eliminar (clase ubicada en utils.py)
                edit_delete_widget = Edit_delete_widget_function(self, row_index, row_data, UpdateUserDialog, self.load_users, self.delete_user)

                # Establecer los botones
                self.tabla_users.setCellWidget(row_index, 6, edit_delete_widget)
                self.tabla_users.setRowHeight(row_index, 50)

        except Exception as e:
            QMessageBox.warning(self.home, "Error", f"Error: {str(e)}")
        finally:
            if conn:
                close_db_connection(conn)



        
    def delete_user(self, user_id, user_name):
        reply = QMessageBox.question(
            self.home,
            "Eliminar usuario",
            f"¿Estás seguro de que quieres eliminar '{user_name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                conn, cursor = get_db_connection()
                if conn is None or cursor is None:
                    raise Exception("No se pudo conectar a la base de datos.")

                cursor.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
                conn.commit()

                QMessageBox.information(self.home, "Eliminado", f"'{user_name}' ha sido eliminado correctamente.")

                self.load_users()  # Recargar la tabla

            except Exception as e:
                QMessageBox.warning(self.home, "Error", f"Error al eliminar: {str(e)}")

            finally:
                if conn:
                    close_db_connection(conn)
