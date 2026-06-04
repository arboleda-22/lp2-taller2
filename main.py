from flask import Flask, render_template, redirect
import sqlite3

app = Flask(__name__)

# 1. AGREGAR esta función para conectar DB
def get_db():
    conexion = sqlite3.connect('productos.db')
    conexion.row_factory = sqlite3.Row  # clave para usar producto['marca']
    return conexion

@app.route('/')
def ruta_raiz():
    # 2. AGREGAR SELECT + render_template
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos ORDER BY tipo, marca")
    productos = cursor.fetchall()
    conn.close()
    return render_template('index.html', productos=productos)

@app.route('/producto/<int:pid>')
def ruta_producto(pid):
    # 3. AGREGAR SELECT por id + render_template
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (pid,))
    producto = cursor.fetchone()
    conn.close()
    
    if producto is None:
        return "Producto no encontrado", 404
    
    return render_template('producto.html', producto=producto)
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

