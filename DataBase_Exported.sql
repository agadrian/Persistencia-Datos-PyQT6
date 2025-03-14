BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS detalles_pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    id_pedido INTEGER NOT NULL, 
    id_plato INTEGER NOT NULL,
    cantidad INTEGER NOT NULL CHECK (cantidad > 0), 
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id) ON DELETE CASCADE, 
    FOREIGN KEY (id_plato) REFERENCES platos(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    id_cliente INTEGER NOT NULL, 
    id_restaurante INTEGER NOT NULL, 
    estado TEXT CHECK (estado IN ('pendiente', 'en preparación', 'en camino', 'entregado')), 
    FOREIGN KEY (id_cliente) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS platos (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nombre TEXT NOT NULL, 
    precio REAL NOT NULL CHECK (precio > 0), 
    descripcion TEXT NOT NULL,
    id_restaurante INTEGER NOT NULL, 
    FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS repartidores (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nif TEXT UNIQUE NOT NULL, 
    nombre TEXT NOT NULL, 
    id_pedido_asignado INTEGER, 
    vehiculo TEXT, 
    FOREIGN KEY (id_pedido_asignado) REFERENCES pedidos(id) ON DELETE SET NULL
);
CREATE TABLE IF NOT EXISTS restaurantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nombre TEXT NOT NULL, 
    direccion TEXT NOT NULL, 
    categoria TEXT, 
    telefono TEXT UNIQUE,
    horario TEXT,
    calificacion REAL CHECK (calificacion >= 0 AND calificacion <= 5)
);
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nombre TEXT NOT NULL, 
    email TEXT UNIQUE NOT NULL, 
    direccion TEXT, 
    telefono TEXT UNIQUE NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "detalles_pedido" ("id","id_pedido","id_plato","cantidad") VALUES (6,6,11,2),
 (7,7,12,1),
 (8,8,13,3),
 (9,9,14,1),
 (10,10,15,2),
 (11,11,16,2),
 (12,12,17,3),
 (13,13,18,1),
 (14,14,19,2),
 (15,10,20,3),
 (16,16,12,1),
 (17,16,17,1),
 (18,17,27,3),
 (19,17,26,2),
 (20,17,20,3),
 (21,17,27,2),
 (22,18,25,3),
 (23,18,24,3),
 (24,18,20,3),
 (25,18,21,2),
 (26,18,27,3),
 (27,19,15,2),
 (28,19,21,2),
 (29,19,19,2),
 (30,20,26,1),
 (31,20,15,3),
 (32,20,11,1),
 (33,20,14,3),
 (34,20,25,1),
 (35,21,22,1),
 (36,21,21,3),
 (37,21,26,3),
 (38,22,23,3),
 (39,22,15,3),
 (40,23,16,3),
 (41,23,28,1),
 (42,23,26,3),
 (43,23,18,3),
 (44,24,24,2),
 (45,24,14,2),
 (46,24,17,2),
 (47,24,17,1),
 (48,25,26,3),
 (49,25,19,2),
 (50,25,13,1),
 (51,25,29,1),
 (52,26,21,2),
 (53,26,18,3),
 (54,26,29,1),
 (55,26,15,1),
 (56,27,11,3),
 (57,27,12,3),
 (58,27,27,1),
 (59,27,29,1),
 (60,27,24,1),
 (61,28,24,3),
 (62,28,13,3),
 (63,29,23,3),
 (64,29,23,1),
 (65,29,30,2),
 (66,30,13,1),
 (67,30,18,3),
 (68,31,21,1),
 (69,31,15,3),
 (70,31,30,3),
 (71,31,14,2),
 (72,31,19,2),
 (73,32,12,2),
 (74,32,22,2),
 (75,32,23,1),
 (76,32,24,2),
 (77,33,24,3),
 (78,33,11,3),
 (79,33,17,2),
 (80,33,15,3),
 (81,33,20,3),
 (82,34,29,3),
 (83,34,17,1),
 (84,34,20,2),
 (85,35,18,2),
 (86,35,30,3),
 (87,35,28,2),
 (88,35,17,1),
 (89,36,27,2),
 (90,36,21,3),
 (91,37,19,1),
 (92,37,15,3),
 (93,38,29,3),
 (94,38,18,3),
 (95,38,11,3),
 (96,38,20,1),
 (97,39,21,2),
 (98,39,27,2),
 (99,39,12,2),
 (100,39,15,2),
 (101,39,18,3),
 (102,40,11,3),
 (103,40,25,3),
 (104,40,22,2),
 (105,40,23,1),
 (106,40,26,2),
 (107,41,30,3),
 (108,41,14,3),
 (109,41,25,2),
 (110,41,27,3),
 (111,42,23,2),
 (112,42,28,1),
 (113,42,16,2),
 (114,42,29,2),
 (115,42,12,3),
 (116,43,14,2),
 (117,43,27,1),
 (118,43,20,2),
 (119,43,27,3),
 (120,44,16,2),
 (121,44,15,3),
 (122,45,13,1),
 (123,45,20,2),
 (124,46,11,2),
 (125,46,25,3),
 (126,46,23,2),
 (127,47,27,2),
 (128,47,22,2),
 (129,47,11,3),
 (130,48,15,3),
 (131,48,24,3),
 (132,48,13,2),
 (133,49,12,3),
 (134,49,26,3),
 (135,49,25,1),
 (136,50,15,2),
 (137,50,14,3),
 (138,50,16,3),
 (139,50,29,2),
 (140,51,22,1),
 (141,51,20,3),
 (142,51,13,1),
 (143,51,29,3),
 (144,51,16,1),
 (145,52,19,1),
 (146,52,25,1),
 (147,52,30,3),
 (148,53,12,1),
 (149,53,28,3),
 (150,54,13,1),
 (151,54,14,2),
 (152,55,21,3),
 (153,55,18,1),
 (154,55,11,2),
 (155,55,28,1),
 (156,55,23,2),
 (157,56,28,2),
 (158,56,24,2),
 (159,56,22,2),
 (160,56,12,2),
 (161,57,15,2),
 (162,57,19,2),
 (163,57,13,2),
 (164,58,23,3),
 (165,58,15,2),
 (166,59,17,2),
 (167,59,26,1),
 (168,59,24,2),
 (169,59,12,3),
 (170,59,20,2),
 (171,60,13,2),
 (172,60,16,2),
 (173,61,21,3),
 (174,61,28,1),
 (175,61,29,3),
 (176,62,30,1),
 (177,62,24,2),
 (178,63,11,1),
 (179,63,18,1),
 (180,63,22,3),
 (181,64,27,1),
 (182,64,11,3),
 (183,64,21,3),
 (184,64,12,1),
 (185,65,21,3),
 (186,65,26,1),
 (187,65,21,1),
 (188,66,16,2),
 (189,66,16,3),
 (190,66,25,3),
 (191,66,20,3),
 (192,66,29,1),
 (193,67,27,1),
 (194,67,21,3),
 (195,67,18,3),
 (196,67,20,1),
 (197,68,19,1),
 (198,68,25,3),
 (199,68,13,3),
 (200,68,21,3),
 (201,69,17,3),
 (202,69,27,1),
 (203,69,29,1),
 (204,70,12,1),
 (205,70,29,3),
 (206,70,24,1),
 (207,71,28,1),
 (208,71,27,2),
 (209,71,26,2),
 (210,71,12,2),
 (211,72,22,2),
 (212,72,28,2),
 (213,72,11,3),
 (214,72,11,1),
 (215,72,12,1),
 (216,73,14,3),
 (217,73,18,1),
 (218,74,13,2),
 (219,74,14,2),
 (220,75,23,2),
 (221,75,16,1),
 (222,76,22,3),
 (223,76,29,1),
 (224,76,28,1),
 (225,76,19,2),
 (226,77,19,3),
 (227,77,17,2),
 (228,77,27,3),
 (229,77,16,1),
 (230,78,15,3),
 (231,78,14,3),
 (232,78,15,3),
 (233,79,26,1),
 (234,79,16,2),
 (235,79,15,1),
 (236,79,22,3),
 (237,79,22,3),
 (238,80,24,2),
 (239,80,21,2),
 (240,80,23,1),
 (241,81,14,3),
 (242,81,22,2),
 (243,81,30,2),
 (244,82,20,3),
 (245,82,28,1),
 (246,82,25,3),
 (247,83,11,3),
 (248,83,18,1),
 (249,83,19,2),
 (250,84,21,2),
 (251,84,12,3),
 (252,85,23,2),
 (253,85,14,1);
INSERT INTO "pedidos" ("id","id_cliente","id_restaurante","estado") VALUES (6,6,11,'pendiente'),
 (7,7,8,'en preparación'),
 (8,8,9,'en camino'),
 (9,9,10,'entregado'),
 (10,15,11,'pendiente'),
 (11,6,12,'en preparación'),
 (12,7,13,'en camino'),
 (13,8,14,'entregado'),
 (14,9,15,'pendiente'),
 (16,17,7,'en preparación'),
 (17,17,10,'entregado'),
 (18,14,9,'en preparación'),
 (19,8,15,'en camino'),
 (20,17,13,'pendiente'),
 (21,6,15,'pendiente'),
 (22,12,13,'entregado'),
 (23,13,13,'pendiente'),
 (24,12,15,'entregado'),
 (25,15,7,'en preparación'),
 (26,17,11,'entregado'),
 (27,18,8,'en camino'),
 (28,18,9,'entregado'),
 (29,7,8,'en camino'),
 (30,15,8,'pendiente'),
 (31,13,11,'en preparación'),
 (32,12,10,'entregado'),
 (33,8,14,'entregado'),
 (34,9,11,'en preparación'),
 (35,13,12,'pendiente'),
 (36,14,8,'entregado'),
 (37,9,15,'entregado'),
 (38,9,15,'pendiente'),
 (39,13,12,'en camino'),
 (40,7,15,'en camino'),
 (41,8,16,'en preparación'),
 (42,8,11,'en preparación'),
 (43,9,9,'en preparación'),
 (44,18,15,'en camino'),
 (45,18,16,'pendiente'),
 (46,8,14,'entregado'),
 (47,9,14,'pendiente'),
 (48,6,12,'en camino'),
 (49,12,15,'en preparación'),
 (50,8,11,'en preparación'),
 (51,13,11,'entregado'),
 (52,19,15,'en camino'),
 (53,7,16,'pendiente'),
 (54,7,13,'en preparación'),
 (55,12,13,'entregado'),
 (56,8,11,'entregado'),
 (57,15,8,'en preparación'),
 (58,17,15,'pendiente'),
 (59,19,14,'en preparación'),
 (60,12,10,'en preparación'),
 (61,17,13,'pendiente'),
 (62,6,14,'en preparación'),
 (63,14,8,'en camino'),
 (64,13,11,'pendiente'),
 (65,13,8,'pendiente'),
 (66,18,15,'en camino'),
 (67,18,8,'en preparación'),
 (68,9,13,'pendiente'),
 (69,8,9,'pendiente'),
 (70,9,16,'en preparación'),
 (71,7,10,'pendiente'),
 (72,6,8,'en camino'),
 (73,18,8,'entregado'),
 (74,8,13,'pendiente'),
 (75,15,9,'en preparación'),
 (76,12,11,'en camino'),
 (77,15,15,'pendiente'),
 (78,13,10,'pendiente'),
 (79,18,12,'entregado'),
 (80,15,8,'en preparación'),
 (81,19,12,'en preparación'),
 (82,14,11,'en camino'),
 (83,12,15,'entregado'),
 (84,9,12,'en camino'),
 (85,8,12,'en preparación');
INSERT INTO "platos" ("id","nombre","precio","descripcion","id_restaurante") VALUES (11,'Pizza Margherita',8.5,'Pizza clásica con tomate, mozzarella y albahaca',14),
 (12,'Spaghetti Carbonara',10.0,'Spaghetti con salsa cremosa de huevo y panceta',14),
 (13,'Sushi Rolls',12.0,'Rollos de sushi con atún, salmón y aguacate',7),
 (14,'Sashimi de Salmón',15.0,'Salmón fresco en láminas finas',7),
 (15,'Tacos al Pastor',6.5,'Tacos de cerdo marinados con piña y cilantro',8),
 (16,'Burritos de Carne',7.0,'Burritos con carne, arroz, frijoles y salsa picante',8),
 (17,'Hamburguesa El Grill',9.0,'Hamburguesa de carne con queso cheddar, cebolla caramelizada',9),
 (18,'Hot Dog con Mostaza',4.5,'Perro caliente con mostaza, ketchup y cebolla',9),
 (19,'Ensalada Vegana',6.0,'Ensalada con quinoa, aguacate, zanahoria y tomate',10),
 (20,'Hamburguesa Vegana',7.5,'Hamburguesa con pan de avena y proteína vegetal',10),
 (21,'Bocadillo de Jamón',5.5,'Bocadillo con jamón serrano y tomate',11),
 (22,'Croquetas Caseras',4.0,'Croquetas de pollo y jamón',11),
 (23,'Arroz Frito',8.0,'Arroz con verduras, pollo y salsa de soja',13),
 (24,'Paella Valenciana',12.5,'Paella con mariscos y pollo',13),
 (25,'Pasta al Pesto',9.0,'Pasta con salsa pesto y piñones',14),
 (26,'Ensalada César',7.0,'Ensalada con pollo, lechuga, crutones y salsa César',14),
 (27,'Pizza Cuatro Quesos',9.5,'Pizza con mozzarella, cheddar, gouda y azul',14),
 (28,'Lasagna Bolognese',11.0,'Lasagna con carne y salsa bechamel',14),
 (29,'Maki Rolls',13.0,'Rollos de sushi con pepino, aguacate y atún',7),
 (30,'Tempura de Mariscos',14.0,'Tempura de camarones y calamares',7);
INSERT INTO "repartidores" ("id","nif","nombre","id_pedido_asignado","vehiculo") VALUES (6,'12345678A','Juan Gómez',6,'bicicleta'),
 (7,'23456789B','Luis Pérez',7,'moto'),
 (8,'34567890C','Marta Periñana',8,'coche'),
 (9,'45678901D','Pedro Sánchez',9,'bicicleta'),
 (10,'56789012E','Isabel Díaz',10,'moto');
INSERT INTO "restaurantes" ("id","nombre","direccion","categoria","telefono","horario","calificacion") VALUES (7,'Sushi Bar Tokyo','Avenida de la Paz 456, Barcelona','Japonesa','923456789','12:00 - 22:00',4.8),
 (8,'El Camino','Calle Mayor 789, Valencia','Mexicana','934567890','10:00 - 24:00',4.2),
 (9,'Restaurante El Grill','Plaza de la Constitución 321, Sevilla','Rápida','945678901','08:00 - 21:00',3.9),
 (10,'La Cantina','Calle de Gran Vía 654, Zaragoza','Vegetariana','956789012','09:00 - 20:00',4.1),
 (11,'El Rincón Andaluz','Calle del Sol 555, Sevilla','Andaluza','967890123','10:00 - 22:00',4.4),
 (12,'El Asador','Calle de la Luna 111, Madrid','Carnes','978901234','12:00 - 23:00',4.6),
 (13,'El Mexicano','Avenida Cataluña 789, Barcelona','Mexicana','989012345','11:00 - 23:00',3.8),
 (14,'La Pizza Nostra','Calle de Alcalá 100, Madrid','Italiana','990123456','12:00 - 23:00',4.7),
 (15,'Café de la Plaza','Plaza Mayor 222, Madrid','Cafetería','991234567','07:00 - 20:00',4.0),
 (16,'Restaurante pruueba','Calle prueba','1','123','123',5.0);
INSERT INTO "usuarios" ("id","nombre","email","direccion","telefono","fecha_registro") VALUES (6,'Juan Pére','juan.perez@example.com','Calle Falsa 123, Madrid','612345678','2025-03-09 20:29:23'),
 (7,'Ana Gómez','ana.gomez@example.com','Avenida de la Paz 456, Barcelona','633456789','2025-03-09 20:29:23'),
 (8,'Carlos Martínez','carlos.martinez@example.com','Calle Mayor 789, Valencia','644567890','2025-03-09 20:29:23'),
 (9,'Laura López','laura.lopez@example.com','Plaza de la Constitución 321, Sevilla','655678901','2025-03-09 20:29:23'),
 (12,'Alberto Ruiz','alberto.ruiz@example.com','Calle San Juan 876, Valencia','688901234','2025-03-09 20:29:23'),
 (13,'Lucía Díaz','lucia.diaz@example.com','Avenida Cataluña 567, Barcelona','699012345','2025-03-09 20:29:23'),
 (14,'Miguel González','miguel.gonzalez@example.com','Calle Princesa 987, Madrid','610123456','2025-03-09 20:29:23'),
 (15,'Pablo Torres','pablo.torres@example.com','Calle de Gran Vía 111, Madrid','611234567','2025-03-09 20:29:23'),
 (17,'Pedro Sánchez','pedro.sanchez@example.com','Calle de Gran Vía 654, Zaragoza','666789012','2025-03-09 20:42:03'),
 (18,'Sofía Pérez','sofia.perez@example.com','Calle de Alcalá 345, Madrid','677890123','2025-03-09 20:42:03'),
 (19,'adriag','1@gmail.com','','656565656','2025-03-09 20:42:51');
COMMIT;
