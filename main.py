from flask import Flask, render_template, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conexion = sqlite3.connect('productos.db')
    conexion.row_factory = sqlite3.Row
    return conexion

@app.route('/')
def ruta_raiz():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos ORDER BY tipo, marca")
    productos = cursor.fetchall()
    conn.close()

    # 1. Lista de fotos en el orden exacto de tu carpeta /static/fotos/
    fotos = ['101.jpg', '104.jpg', '201.jpg', '203.jpg', '207.jpg', '208.jpg', '301.jpg', '302.jpg', '304.jpg']
    
    # 2. Empareja producto con foto por posición: producto 1 con foto 1, etc
    productos_con_foto = list(zip(productos, fotos))
    
    return render_template('index.html', productos_con_foto=productos_con_foto)

@app.route('/producto/<int:pid>')
def ruta_producto(pid):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (pid,))
    producto = conn.cursor().execute("SELECT * FROM productos WHERE id = ?", (pid,)).fetchone()
    conn.close()
    
    if producto is None:
        return "Producto no encontrado", 404
    
    return render_template('producto.html', producto=producto)
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
    

