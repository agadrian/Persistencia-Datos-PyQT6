from dialogs.CreateUserDialog import *
from db_functions import *
from utils import *
from PDFGenerator import PDFGenerator

class homePage(QWidget):
    def __init__(self, home_window):
        super().__init__()
        self.home = home_window

        # Conectar botones - linedits

        # Query 1
        self.pushButton_crossAnalysis = self.home.pushButton_crossAnalysis
        
        # Query 2
        self.pushButton_getTopRestaurants = self.home.pushButton_getTopRestaurants

        # Query 3
        self.pushButton_getConsum = self.home.pushButton_getConsum

        # Query 4
        self.pushButton_getbutn = self.home.pushButton_getbutn

        # Query 5
        self.pushButton_getRestDishes_5 = self.home.pushButton_getRestDishes_5

        # Query 6
        self.pushButton_getRestDishes = self.home.pushButton_getRestDishes
        self.lineEdit_allRestaurantDishes = self.home.lineEdit_allRestaurantDishes

        
        

        
        # Layout principal
        self.layout = QVBoxLayout(self)

        self.current_table = None

        ## Ejecutar las consultas al hacer click al botón

        # Query 1 - Análisis Cruzado de Usuarios, Platos y Categorías
        self.pushButton_crossAnalysis.clicked.connect(lambda: self.fetch_data(
            query= """
            WITH PlatosPorUsuario AS (
                SELECT 
                    u.id AS IdUsuario,
                    u.nombre AS NombreUsuario,
                    pl.id AS IdPlato,
                    pl.nombre AS NombrePlato,
                    r.categoria AS CategRest,
                    COUNT(DISTINCT p.id) AS VecesPedido,
                    SUM(dp.cantidad) AS CantTotal,
                    SUM(pl.precio * dp.cantidad) AS GastoPlato
                FROM usuarios u
                JOIN pedidos p ON u.id = p.id_cliente
                JOIN detalles_pedido dp ON p.id = dp.id_pedido
                JOIN platos pl ON dp.id_plato = pl.id
                JOIN restaurantes r ON p.id_restaurante = r.id
                GROUP BY u.id, pl.id
            ),
            PlatosFavoritos AS (
                SELECT 
                    IdUsuario,
                    IdPlato,
                    NombrePlato,
                    VecesPedido,
                    ROW_NUMBER() OVER (PARTITION BY IdUsuario ORDER BY VecesPedido DESC, CantTotal DESC) AS Ranking
                FROM PlatosPorUsuario
            ),
            CategoriasFavoritas AS (
                SELECT 
                    IdUsuario,
                    CategRest,
                    COUNT(DISTINCT IdPlato) AS PlatosDif,
                    SUM(GastoPlato) AS GastoCateg,
                    ROW_NUMBER() OVER (PARTITION BY IdUsuario ORDER BY SUM(GastoPlato) DESC) AS Ranking
                FROM PlatosPorUsuario
                GROUP BY IdUsuario, CategRest
            ),
            ResumenUsuario AS (
                SELECT 
                    u.id AS IdUsuario,
                    u.nombre AS NombreUsuario,
                    COUNT(DISTINCT p.id) AS TotalPedidos,
                    COUNT(DISTINCT p.id_restaurante) AS RestDif,
                    SUM(pl.precio * dp.cantidad) AS GastoTotal
                FROM usuarios u
                JOIN pedidos p ON u.id = p.id_cliente
                JOIN detalles_pedido dp ON p.id = dp.id_pedido
                JOIN platos pl ON dp.id_plato = pl.id
                GROUP BY u.id
            )
            SELECT 
                ru.NombreUsuario,
                ru.TotalPedidos,
                ru.RestDif,
                ROUND(ru.GastoTotal, 2) AS GastoTotal,
                pf.NombrePlato AS PlatoFav,
                pf.VecesPedido AS VecesPedidoFav,
                cf.CategRest AS CategFav,
                cf.PlatosDif AS PlatosDifCateg,
                ROUND(cf.GastoCateg, 2) AS GastoCategFav,
                ROUND(cf.GastoCateg * 100.0 / ru.GastoTotal, 2) AS PctGastoCateg,
                CASE 
                    WHEN ru.TotalPedidos > 5 THEN 'Frecuente'
                    WHEN ru.TotalPedidos > 2 THEN 'Regular'
                    ELSE 'Ocasional'
                END AS TipoCliente
            FROM ResumenUsuario ru
            JOIN PlatosFavoritos pf ON ru.IdUsuario = pf.IdUsuario AND pf.Ranking = 1
            JOIN CategoriasFavoritas cf ON ru.IdUsuario = cf.IdUsuario AND cf.Ranking = 1
            ORDER BY ru.GastoTotal DESC;

            """,
            title= "Análisis Cruzado de Usuarios, Platos y Categorías",
            PDFName= "Informe_Analisis_Usuarios_Platos_Categorias",
            emptyMsg= "No hay datos disponibles para esta consulta."
            )
        )

        # Query 2 
        self.pushButton_getTopRestaurants.clicked.connect(lambda: self.fetch_data(
            query= """
                WITH VentasPorRestaurante AS (
                    SELECT 
                        r.id,
                        r.nombre AS NombreRest,
                        r.categoria AS Categoria,
                        r.calificacion AS Calificacion,
                        COUNT(DISTINCT p.id) AS PedidosTotal,
                        SUM(pl.precio * dp.cantidad) AS TotalVentas,
                        COUNT(DISTINCT p.id_cliente) AS ClientesUnicos
                    FROM restaurantes r
                    JOIN pedidos p ON r.id = p.id_restaurante
                    JOIN detalles_pedido dp ON p.id = dp.id_pedido
                    JOIN platos pl ON dp.id_plato = pl.id
                    GROUP BY r.id
                )
                SELECT 
                    NombreRest,
                    Categoria,
                    Calificacion,
                    PedidosTotal,
                    ClientesUnicos,
                    ROUND(TotalVentas, 2) AS TotalVentas,
                    ROUND(TotalVentas / NULLIF(PedidosTotal, 0), 2) AS TicketPromedio,
                    ROUND(ClientesUnicos * 100.0 / NULLIF(PedidosTotal, 0), 2) AS IndiceFidelizac
                FROM VentasPorRestaurante
                ORDER BY TotalVentas DESC;

                """,
            title= "Top 5 Restaurantes por volumen de ventas",
            PDFName= "Informe_restaurantes_volumen_ventas",
            emptyMsg= "No hay datos disponibles para esta consulta."
            )
        )

        # Query 3
        self.pushButton_getConsum.clicked.connect(lambda: self.fetch_data(
            query= """
                WITH GastosPorCliente AS (
                    SELECT 
                        u.id AS id_cliente,
                        u.nombre AS Nombre,
                        COUNT(DISTINCT p.id) AS PedidosTotal,
                        SUM(pl.precio * dp.cantidad) AS GastoTotal,
                        MAX(p.id) AS ultimo_pedido_id,
                        COUNT(DISTINCT r.categoria) AS CategsDif
                    FROM usuarios u
                    JOIN pedidos p ON u.id = p.id_cliente
                    JOIN detalles_pedido dp ON p.id = dp.id_pedido
                    JOIN platos pl ON dp.id_plato = pl.id
                    JOIN restaurantes r ON p.id_restaurante = r.id
                    GROUP BY u.id
                ),
                CategoriasPorCliente AS (
                    SELECT 
                        u.id AS id_cliente,
                        r.categoria,
                        COUNT(DISTINCT p.id) AS NumPedidosCateg,
                        ROW_NUMBER() OVER (PARTITION BY u.id ORDER BY COUNT(DISTINCT p.id) DESC) AS ranking
                    FROM usuarios u
                    JOIN pedidos p ON u.id = p.id_cliente
                    JOIN restaurantes r ON p.id_restaurante = r.id
                    GROUP BY u.id, r.categoria
                ),
                UltimoPedido AS (
                    SELECT 
                        gc.id_cliente,
                        r.nombre AS UltimoRest,
                        p.estado AS UltPedido
                    FROM GastosPorCliente gc
                    JOIN pedidos p ON gc.ultimo_pedido_id = p.id
                    JOIN restaurantes r ON p.id_restaurante = r.id
                )
                SELECT 
                    gc.nombre,
                    gc.pedidosTotal,
                    ROUND(gc.gastoTotal, 2) AS GastoTotal,
                    ROUND(gc.gastoTotal / NULLIF(gc.pedidosTotal, 0), 2) AS GastoProm,
                    cp.categoria AS CategPrefe,
                    gc.categsDif,
                    up.ultimoRest,
                    up.ultPedido
                FROM GastosPorCliente gc
                JOIN CategoriasPorCliente cp ON gc.id_cliente = cp.id_cliente AND cp.ranking = 1
                JOIN UltimoPedido up ON gc.id_cliente = up.id_cliente
                ORDER BY gc.gastoTotal DESC;

                """,
            title= "Análisis de Clientes y sus Hábitos de Consumo",
            PDFName= "Informe_Analisis_Clientes",
            emptyMsg= "No hay datos disponibles para esta consulta."
            )
        )

        # Query 4
        self.pushButton_getbutn.clicked.connect(lambda: self.fetch_data(
            query= """
            WITH VentasPlatos AS (
                SELECT 
                    pl.id AS PlatoID,
                    pl.nombre AS NombrePlato,
                    pl.precio AS Precio,
                    r.id AS RestauranteID,
                    r.nombre AS NombreRest,
                    r.categoria AS CategRestaurante,
                    SUM(dp.cantidad) AS UndsVendidas,
                    COUNT(DISTINCT p.id) AS AparicionesPedidos,
                    SUM(pl.precio * dp.cantidad) AS IngresosGenerados
                FROM platos pl
                JOIN detalles_pedido dp ON pl.id = dp.id_plato
                JOIN pedidos p ON dp.id_pedido = p.id
                JOIN restaurantes r ON p.id_restaurante = r.id
                GROUP BY pl.id
            ),
            TotalVentasRestaurante AS (
                SELECT 
                    restauranteID,
                    SUM(IngresosGenerados) AS TotalIngresosRest
                FROM VentasPlatos
                GROUP BY restauranteID
            ),
            RankingGlobal AS (
                SELECT 
                    *,
                    RANK() OVER (ORDER BY IngresosGenerados DESC) AS RankingIngresos
                FROM VentasPlatos
            )
            SELECT 
                rg.NombrePlato,
                rg.Precio,
                rg.NombreRest,
                rg.CategRestaurante,
                rg.UndsVendidas,
                rg.AparicionesPedidos,
                ROUND(rg.IngresosGenerados, 2) AS IngresosGenerados,
                rg.RankingIngresos,
                CASE 
                    WHEN rg.RankingIngresos <= 5 THEN 'Muy popular'
                    WHEN rg.RankingIngresos <= 10 THEN 'Popular'
                    WHEN rg.RankingIngresos <= 15 THEN 'Moderado'
                    ELSE 'Poco popular'
                END AS NivelPopularidad
            FROM RankingGlobal rg
            JOIN TotalVentasRestaurante tvr ON rg.RestauranteID = tvr.RestauranteID
            ORDER BY rg.UndsVendidas DESC;

            """,
            title= "Análisis de Popularidad de Platos y Rentabilidad",
            PDFName= "Informe_Analisis_Popularidad_Platos",
            emptyMsg= "No hay datos disponibles para esta consulta."
            )
        )

        # Query 5
        self.pushButton_getRestDishes_5.clicked.connect(lambda: self.fetch_data(
            query= """
                WITH EstadisticasPedidos AS (
                SELECT 
                    r.id AS RestauranteID,
                    r.nombre AS NombreRest,
                    r.categoria AS Categoria,
                    r.calificacion AS Calificacion,
                    COUNT(p.id) AS TotalPedidos,
                    SUM(CASE WHEN p.estado = 'entregado' THEN 1 ELSE 0 END) AS Entregados,
                    SUM(CASE WHEN p.estado = 'en camino' THEN 1 ELSE 0 END) AS EnCamino,
                    SUM(CASE WHEN p.estado = 'en preparación' THEN 1 ELSE 0 END) AS EnPreparacion,
                    SUM(CASE WHEN p.estado = 'pendiente' THEN 1 ELSE 0 END) AS Pendientes
                FROM restaurantes r
                LEFT JOIN pedidos p ON r.id = p.id_restaurante
                GROUP BY r.id
            ),
            PromediosPorCategoria AS (
                SELECT 
                    Categoria,
                    AVG(Entregados * 100.0 / CASE WHEN TotalPedidos = 0 THEN 1 ELSE TotalPedidos END) AS PromedioEntregadosCateg
                FROM EstadisticasPedidos
                GROUP BY Categoria
            )
            SELECT 
                ep.NombreRest,
                ep.Categoria,
                ep.Calificacion,
                ep.TotalPedidos,
                ep.Entregados,
                ep.EnCamino,
                ep.EnPreparacion,
                ep.Pendientes,
                ROUND(ep.Entregados * 100.0 / CASE WHEN ep.TotalPedidos = 0 THEN 1 ELSE ep.TotalPedidos END, 2) AS PctjeCompeltados,
                ROUND(ppc.PromedioEntregadosCateg, 2) AS PromedioCateg
            FROM EstadisticasPedidos ep
            JOIN PromediosPorCategoria ppc ON ep.Categoria = ppc.Categoria
            ORDER BY PctjeCompeltados DESC;
            """,
            title= "Análisis de Eficiencia de Restaurantes por Estado de Pedidos",
            PDFName= "Informe_Eficiencia_Restaurantes",
            emptyMsg= "No hay datos disponibles para esta consulta."
            )
        )


        # Query 6
        self.pushButton_getRestDishes.clicked.connect(lambda: self.fetch_data(
            query= """
            WITH HistorialPedidos AS (
                SELECT 
                    p.id AS IdPedido,
                    u.nombre AS NombreUsuario,
                    r.nombre AS NombreRest,
                    r.categoria AS CategRest,
                    p.estado AS EstadoPedido,
                    SUM(dp.cantidad * pl.precio) AS TotalGastado
                FROM pedidos p
                JOIN usuarios u ON p.id_cliente = u.id
                JOIN restaurantes r ON p.id_restaurante = r.id
                JOIN detalles_pedido dp ON p.id = dp.id_pedido
                JOIN platos pl ON dp.id_plato = pl.id
                WHERE p.id_cliente = ?
                GROUP BY p.id
            ),
            DetallesPlatos AS (
                SELECT 
                    p.id AS IdPedido,
                    GROUP_CONCAT(pl.nombre || ' (x' || dp.cantidad || ')', ', ') AS PlatosPedidos
                FROM pedidos p
                JOIN detalles_pedido dp ON p.id = dp.id_pedido
                JOIN platos pl ON dp.id_plato = pl.id
                WHERE p.id_cliente = ?
                GROUP BY p.id
            )
            SELECT 
                hp.IdPedido,
                hp.NombreUsuario,
                hp.NombreRest,
                hp.CategRest,
                hp.EstadoPedido,
                hp.TotalGastado,
                dp.PlatosPedidos
            FROM HistorialPedidos hp
            LEFT JOIN DetallesPlatos dp ON hp.IdPedido = dp.IdPedido
            ORDER BY hp.IdPedido DESC;


            """,
            title= f"Historial de pedidos de el usuario ID {self.lineEdit_allRestaurantDishes.text().strip()}",
            PDFName= f"Hisorial pedidos usuario ID {self.lineEdit_allRestaurantDishes.text().strip()}",
            params= (self.lineEdit_allRestaurantDishes.text().strip(),self.lineEdit_allRestaurantDishes.text().strip()),
            emptyMsg= "No hay datos disponibles para esta consulta."
            )
        )
        


    def create_table(self, headers, data):
        """ Crea una nueva QTableWidget con los datos de la consulta. """
        # Si hay una tabla previa, la eliminamos
        if self.current_table:
            self.layout.removeWidget(self.current_table)
            self.current_table.deleteLater()
            self.current_table = None

        # Crear una nueva tabla con el número de columnas dinámico
        table = QTableWidget(self)
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.setAlternatingRowColors(True)

        # Insertar los datos en la tabla
        for row_index, row_data in enumerate(data):
            table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                table.setItem(row_index, col_index, item)

        # Guardamos la tabla actual y la agregamos al layout
        self.current_table = table
        self.layout.addWidget(self.current_table)

        

    

    def execute_query(self, query, params=()):
        """ Ejecuta una consulta y devuelve los resultados. """
        try:
            conn, cursor = get_db_connection()
            cursor.execute(query, params)
            data = cursor.fetchall()
            headers = [desc[0] for desc in cursor.description]  
            return headers, data
        except Exception as e:
            QMessageBox.warning(self.home, "Error", f"Error ejecutando la consulta: {str(e)}")
            return [], []
        finally:
            close_db_connection(conn)
    

    def fetch_data(self, query, title, PDFName, emptyMsg, params = ()):
        """ Ejecuta una consulta genérica y genera una tabla y un PDF con los resultados. """

        # Eliminar espacios en blanco en los parámetros y filtrar vacíos
        params = tuple(param.strip() for param in params if param.strip())

        necesita_params = "?" in query

        if necesita_params and not params:
            QMessageBox.warning(self.home, "Error", "Debe ingresar un ID válido.")
            return

        # Ejecutar la consulta con o sin parámetros
        headers, data = self.execute_query(query, params) if necesita_params else self.execute_query(query)

    
        self.create_table(headers, data)
        self.export_pdf(title, PDFName, emptyMsg=emptyMsg)



    
    def export_pdf(self, title, PDFName, emptyMsg):
        if not PDFName.endswith(".pdf"):
            PDFName += ".pdf"
        pdf = PDFGenerator()
        pdf.generate_table_from_qtwidget(self.current_table, emptyMsg=emptyMsg, title=title)
        pdf.save(PDFName)
        QMessageBox.information(self.home, "Exito", f"PDF creado correctamente dentro de Informes")
    
