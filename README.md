# App: Just Meat

## Logo corporativo

![logo](ui/res/logo.png)

## Tipo de letra

- Titulos menú: Roboto
- Texto: Segoe UI

## Color corporativo

Hemos decidido usar el verde como color corporativo, ya que compagina bien con la temática de la empresa

## Explicación funcionamiento

Se ha creado una App con un login y registro de usuarios, haciendo uso de Fireabse auth.

Por otro lado, se ha creado varias tablas en SQLite con información relacionada, para las cuales hay una tabla con la que hacer las operaciones basicas (CRUD).

Por último, hay una página donde hacer una serie de consultas preestablecidas.


## Diagrama E-R

Archivo .SQL exportado de la base de datos: [**.SQL**](DataBase_Exported.sql)

![diagrama](ui/res/diagrama.png)



## Usuarios en FireBase y Localmente

- El usuario usado para testear ha sido adriag. Para hacer login, usar: 1@gmail.com con contraseña: 123123aA. 

![usuarios](ui/res/usersScreenshoot.png)

![usuarios](ui/res/usersScreenshoot2.png)

## Utilidades

- Login y registro de usuarios, insertandolos en Firebase y en SQLite (exceptuando datos como la contraseña, por temas de seguridad)
- CRUD de la tabla usuarios, y 5 más.
- Crear reportes de consultas, alguna de ella personalizada por medio de la ID de usuario.
- Como extra se ha añadido una exportación de datos de las tablas completas individualmente a PDF mediante el uso de la librería FPDF.

 

## Empaquetar la App

Haciendo uso de PyInstaller, usando este comando he empaquetado todo

**pyinstaller --name "JustMeatApp" --add-data "database.db;." --add-data "ui/pages;ui/pages" --add-data "ui/dialogs;ui/dialogs" --add-data "ui/res;ui/res" --add-data "dialogs;dialogs" --add-data ".env;." --windowed main.py**

La App empaquetada se encuentra en la siguiente carpeta del repositorio: [JustMeatApp](AppEmpaquetada)

Los PDFS se exportan en la ruta [**_internal/Reports**](AppEmpaquetada/dist/JustMeatApp/_internal/Reports)
