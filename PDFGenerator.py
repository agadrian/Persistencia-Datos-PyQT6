from fpdf import FPDF
from PyQt6.QtWidgets import QTableWidget, QApplication
import sys
from datetime import datetime
import os
import textwrap
from utils import resource_path

class PDFGenerator(FPDF):
    def __init__(self, orientation='L', unit='mm', format='A4'):
        super().__init__(orientation, unit, format)

        # Desactivar auto paginado
        self.set_auto_page_break(auto=False, margin=15)  
        self.add_page()
        self.set_font('Arial', '', 12)

    def header(self):
        # Logo empresa
        logo_path = resource_path('ui/res/logo.png')
        self.image(logo_path, 10, 12, 30, 30)
        self.set_y(25)

        # Titulo empresa
        self.set_font('Arial', 'B', 20)
        self.cell(0, 10, 'Just Meat S.L', 0, 0, 'C')

        #Hora de creacion de informe
        self.set_font('Arial', '', 10)
        self.cell(0, 10, f"Creación informe: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", 0, 1, 'R') 
        self.ln(15)

    def footer(self):
        self.set_y(-15)

        # Contacto en el centro
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Just Meat S.L - Contacto: info@justmeat.com', 0, 0, 'C')

        # Número de página alineado a la derecha
        self.set_x(-30)  
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'R')
       

    def add_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 8, title, 0, 1, 'C')
        self.ln(10)

    def add_table_headers(self, headers, col_widths):
        """Dibuja los encabezados de la tabla en la página."""
        self.set_font('Arial', 'B', 10)
        self.set_fill_color(200, 230, 200)  # Verde claro
        for i, header in enumerate(headers):
            self.cell(col_widths[i], 10, header, 1, 0, 'C', 1)
        self.ln()




    def generate_table_from_qtwidget(self, table_widget, emptyMsg="No hay datos disponibles", title="Reporte de Datos"):
        # Agregar el título del reporte
        self.add_title(title)

        # Obtener el número de filas y columnas de la tabla
        rows = table_widget.rowCount()
        cols = table_widget.columnCount() 

        # Verificar si la tabla está vacía
        if rows == 0 or cols == 0:
            self.set_font('Arial', 'I', 12)
            self.multi_cell(0, 10, emptyMsg, 0, 'C')
            return

        # Obtener encabezados de la tabla
        headers = [table_widget.horizontalHeaderItem(col).text() if table_widget.horizontalHeaderItem(col) else f"Columna {col+1}" for col in range(cols)]
        
        # Calcular anchos iniciales de columnas
        col_widths = [self.get_string_width(header) + 4 for header in headers]

        # Ajustar tamaños de columna basados en el contenido
        for col in range(cols):
            max_width = col_widths[col]
            for row in range(rows):
                item = table_widget.item(row, col)
                if item:
                    text_width = self.get_string_width(item.text()) + 4
                    max_width = min(max(max_width, text_width), 50)  # Limitar el ancho máximo
            col_widths[col] = max_width

        # Ajustar el ancho de las columnas si excede el ancho de la página
        page_width = self.w - 16  # Considerar márgenes
        total_width = sum(col_widths)
        if total_width > page_width:
            ratio = page_width / total_width
            col_widths = [width * ratio for width in col_widths]

        # Agregar encabezados de la tabla al PDF
        self.add_table_headers(headers, col_widths)

        # Configurar fuente para el contenido de la tabla
        self.set_font('Arial', '', 10)
        font_size = 9
        avg_char_width = self.get_string_width('a')

        # Recorrer filas de la tabla
        for row in range(rows):
            row_data = []
            max_lines = 1

            # Recorrer columnas de la tabla
            for col in range(cols):
                item = table_widget.item(row, col)
                text = item.text() if item else ""
                chars_per_line = max(int((col_widths[col] - 4) / avg_char_width), 1)
                lines = textwrap.wrap(text, width=chars_per_line) if len(text) > chars_per_line else [text]
                row_data.append(lines)
                max_lines = max(max_lines, len(lines))

            # Calcular altura de la celda
            line_height = max(6, font_size / 2 + 2)
            cell_height = line_height * max_lines

            # Verificar si hay espacio suficiente en la página antes de imprimir
            if self.get_y() + cell_height > self.h - 20:
                self.add_page()
                self.ln(10)  # Espacio entre cabecera de la tabla y título
                self.add_table_headers(headers, col_widths)
                
            # Dibujar la fila
            y_pos = self.get_y()
            for col in range(cols):
                x_pos = self.get_x()
                self.rect(x_pos, y_pos, col_widths[col], cell_height)  # Dibujar borde de la celda
                content_lines = row_data[col]
                v_padding = (cell_height - (len(content_lines) * line_height)) / 2  # Ajustar alineación vertical
                for i, line in enumerate(content_lines):
                    line_y = y_pos + v_padding + (i * line_height)
                    self.set_xy(x_pos, line_y)
                    self.cell(col_widths[col], line_height, line, 0, 0, 'C')
                self.set_x(x_pos + col_widths[col])
            self.set_y(y_pos + cell_height)

    def save(self, filename):
        # Obtener el directorio de informes y crearlo si no existe
        informes_dir = resource_path("Reports")
        if not os.path.exists(informes_dir):
            os.makedirs(informes_dir)

        # Generar nombre de archivo con timestamp
        base_filename = os.path.basename(filename)
        timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        name, ext = os.path.splitext(base_filename)
        new_filename = f"{name}_{timestamp}{ext}"
        full_path = os.path.join(informes_dir, new_filename)

        # Guardar el archivo PDF
        self.output(full_path)
        return full_path
