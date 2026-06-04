# importar la librería para gestionar la DB
import sqlite3

# establecer la conexion
conection = sqlite3.connect('productos.db')

# crear un cursor
cursor = conection.cursor()

# eliminar la tabla
cursor.execute("DROP TABLE IF EXISTS productos;")

# crear la tabla
cursor.execute("""
CREATE TABLE productos (
  id INTEGER PRIMARY KEY,
  tipo TEXT NOT NULL,
  marca TEXT NOT NULL,
  modelo TEXT NOT NULL,
  descripcion TEXT,
  precio INTEGER NOT NULL
);

""")

# insertar los datos iniciales
datos = [
  (101, 'Celular', 'Apple', 'iPhone 15', '128GB+6GB RAM, Pantalla 6.1p, Chip A16 Bionic, cable Tipo C, Cámara 48MP', 4599900),
  (104, 'Celular', 'Samsung', 'Galaxy S23', '256GB+8GB RAM, Pantalla 6p, Chip SM8550 Octacore, cámaras 50MP+10MP+12MP', 3499900),
  (201, 'Portátil', 'Apple', 'Macbook Pro M2', 'Chip Apple M2 Pro 10cores+16gpu, 16Gb RAM, 512Gb SSD, Pantalla 13p, Gráficos ', 15749900),
  (203, 'Portátil', 'Asus', 'Laptop ROG Zephyrus', 'Cpu RYZEN 9-6900HS, 24Gb RAM, 2Tb SSD, Gráficos RTX-3060 6GB, Pantalla 15,6', 8819900),
  (207, 'Portátil', 'HP', 'Laptop 14-fq1012la', 'Cpu AMD Ryzen 5, 12Gb RAM, 256Gb SSD, Pantalla 14p, Wifi, Lan, 2 USB-C, HDMI, ', 1799000),
  (208, 'Portátil', 'Lenovo', 'Todo en Uno', 'Cpu AMD RYZEN 7-5700U, 2Tb SSD, 8Gb RAM, Pantalla 23.8, Wifi, Lan, 2 USB-C, HDMI', 4569900),
  (301, 'Tablet', 'Apple', 'iPad 10gen', '64Gb, Pantalla 10.9p, USB-C, Wifi', 2799000),
  (302, 'Tablet', 'Amazon', 'Kindle Oasis 10gen', '32Gb, Pantalla 7p, USB-C, Wifi', 1390000),
  (304, 'Tablet', 'Huawei', 'MatePad SE 10.1', '128Gb, Pantalla 10.1p 2K, USB-C, Wifi', 931000),
]

cursor.executemany("""
INSERT INTO productos (
  id,
  tipo,
  marca,
  modelo,
  descripcion,
  precio
) VALUES (?, ?, ?, ?, ?, ?);
""", datos)

# grabar
conection.commit()
conection.close()
