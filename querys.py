from dialogs.CreateUserDialog import *
from db_functions import *
from utils import *
from PDFGenerator import PDFGenerator
from PyQt6.QtWidgets import QHeaderView


class querysPage(QWidget):
    def __init__(self, home_window):
        super().__init__()
        self.home = home_window

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.tableWidget = self.home.tableWidget

        # Conectar botones

        # Query 1
        self.pushButton_q1 = self.home.pushButton_q1
        self.pushButton_q1.clicked.connect(lambda: self.fetch_data(
            query= """
            SELECT 
                r.nombre AS Restaurant, 
                r.calificacion AS Rating, 
                r.categoria AS Category,
                p.nombre AS MostExpensiveDish, 
                p.precio AS Price,
                COUNT(dp.id) AS TimesOrdered
            FROM restaurantes r
            JOIN platos p ON r.id = p.id_restaurante
            LEFT JOIN detalles_pedido dp ON p.id = dp.id_plato
            WHERE p.precio = (
                SELECT MAX(precio) 
                FROM platos 
                WHERE id_restaurante = r.id
            )
            GROUP BY r.id, p.id
            ORDER BY r.calificacion DESC, TimesOrdered DESC
            LIMIT 5;
                """
        ))

        # Query 2
        self.pushButton_q2 = self.home.pushButton_q2
        self.pushButton_q2.clicked.connect(lambda: self.fetch_data(
            query= """
                SELECT 
                u.nombre AS Customer,
                u.email AS Email,
                COUNT(p.id) AS TotalOrders,
                r.nombre AS FavoriteRestaurant,
                r.categoria AS Category,
                MAX(r.calificacion) AS Rating
            FROM usuarios u
            JOIN pedidos p ON u.id = p.id_cliente
            JOIN restaurantes r ON p.id_restaurante = r.id
            GROUP BY u.id
            HAVING COUNT(p.id) > 1
            ORDER BY TotalOrders DESC;
                """
        ))


         # Query 3
        self.pushButton_q3 = self.home.pushButton_q3
        self.pushButton_q3.clicked.connect(lambda: self.fetch_data(
            query= """
                SELECT 
                rep.nombre AS DeliveryPerson,
                rep.vehiculo AS Vehicle,
                COUNT(p.id) AS TotalOrders,
                SUM(CASE WHEN p.estado = 'entregado' THEN 1 ELSE 0 END) AS DeliveredOrders,
                SUM(CASE WHEN p.estado = 'en camino' THEN 1 ELSE 0 END) AS OrdersInTransit,
                ROUND(SUM(CASE WHEN p.estado = 'entregado' THEN 1 ELSE 0 END) * 100.0 / COUNT(p.id), 2) AS SuccessRate
            FROM repartidores rep
            LEFT JOIN pedidos p ON rep.id_pedido_asignado = p.id
            GROUP BY rep.id
            ORDER BY SuccessRate DESC;
                """
        ))

         # Query 4
        self.pushButton_q4 = self.home.pushButton_q4
        self.pushButton_q4.clicked.connect(lambda: self.fetch_data(
            query= """
                SELECT 
                r.categoria AS Category,
                p.nombre AS Dish,
                p.precio AS Price,
                SUM(dp.cantidad) AS TotalQuantity,
                COUNT(DISTINCT p.id_restaurante) AS NumberOfRestaurants,
                AVG(r.calificacion) AS AverageRating
            FROM platos p
            JOIN restaurantes r ON p.id_restaurante = r.id
            JOIN detalles_pedido dp ON p.id = dp.id_plato
            GROUP BY r.categoria, p.nombre
            ORDER BY r.categoria, TotalQuantity DESC;
            """
        ))


        # Query 5
        self.pushButton_q5 = self.home.pushButton_q5
        self.pushButton_q5.clicked.connect(lambda: self.fetch_data(
            query= """
                SELECT 
                u.id AS Id,
                u.nombre AS CustomerName,
                u.email AS Email,
                u.fecha_registro AS RegistrationDate,
                COUNT(DISTINCT p.id) AS TotalOrders
            FROM usuarios u
            LEFT JOIN pedidos p ON u.id = p.id_cliente
            WHERE u.id NOT IN (
                SELECT DISTINCT p.id_cliente
                FROM pedidos p
                JOIN restaurantes r ON p.id_restaurante = r.id
                WHERE r.categoria = 'Italiana'
            )
            GROUP BY u.id
            HAVING COUNT(DISTINCT p.id) > 0
            ORDER BY TotalOrders DESC;
            """
        ))


        # Query 6
        self.pushButton_q6 = self.home.pushButton_q6
        self.pushButton_q6.clicked.connect(lambda: self.fetch_data(
            query= """
                SELECT 
                r.nombre AS Restaurant,
                r.direccion AS Address,
                COUNT(p.id) AS PendingOrders,
                rep.nombre AS DeliveryPerson,
                rep.vehiculo AS Vehicle,
                MAX(u.nombre) AS LastCustomer,
                MAX(pl.nombre) AS MostRecentDish
            FROM restaurantes r
            JOIN pedidos p ON r.id = p.id_restaurante
            JOIN usuarios u ON p.id_cliente = u.id
            LEFT JOIN repartidores rep ON rep.id_pedido_asignado = p.id
            JOIN detalles_pedido dp ON p.id = dp.id_pedido
            JOIN platos pl ON dp.id_plato = pl.id
            WHERE p.estado IN ('pendiente', 'en preparación')
            GROUP BY r.id, rep.id
            ORDER BY PendingOrders DESC;
            """
        ))
        
    


        '''# Espacio de cada columna de la tabla
        self.tabla_users.setColumnWidth(0, 40)
        self.tabla_users.setColumnWidth(1, 140)
        self.tabla_users.setColumnWidth(2, 170)
        self.tabla_users.setColumnWidth(3, 170)
        self.tabla_users.setColumnWidth(4, 120)
        self.tabla_users.setColumnWidth(5, 120)
        self.tabla_users.setColumnWidth(6, 100)'''
    
    

    def update_table(self, headers, data):
        """Crea una QTableWidget y la muestra en la interfaz"""
        table = self.home.tableWidget  # Usa la tabla creada en Qt Designer
        table.clear()  # Limpia la tabla antes de llenarla

        # Configurar encabezados
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)

        # Insertar datos en la tabla
        table.setRowCount(len(data))
        for row_index, row_data in enumerate(data):
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                table.setItem(row_index, col_index, item)

        table.resizeColumnsToContents()  # Ajustar columnas al contenido
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
  # Ajustar columnas al ancho total
        table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)



    def execute_query(self, query):
        """Ejecuta una consulta y devuelve los resultados"""
        try:
            conn, cursor = get_db_connection()
            cursor.execute(query)
            data = cursor.fetchall()
            headers = [desc[0] for desc in cursor.description]
            print(headers, data)
            return headers, data
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error ejecutando la consulta: {str(e)}")
            return [], []
        finally:
            if conn:
                close_db_connection(conn)
            



    def fetch_data(self, query):
        """Ejecuta una consulta y muestra los resultados en una tabla"""
    
        headers, data = self.execute_query(query)
        if headers:
            self.update_table(headers, data)
        else:
            QMessageBox.information(self, "Sin datos", "No se encontraron resultados.")
    
