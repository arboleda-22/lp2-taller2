from flask import Flask, render_template, redirect
import sqlite3

app = Flask(_name_)

def get_db():
    conexion = sqlite3.connect('productos.db')
    conexion.row_factory = sqlite3.Row
    return conexion

@app.route('/')
def ruta_raiz():
    # Página de bienvenida solo con banner y botón
    return render_template('index.html')

@app.route('/catalogo')
def ruta_catalogo():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos ORDER BY id")  # respeta orden de fotos
    productos = cursor.fetchall()
    conn.close()

    fotos = ['101.jpg', '104.jpg', '201.jpg', '203.jpg', '207.jpg', '208.jpg', '301.jpg', '302.jpg', '304.jpg']
    productos_con_foto = list(zip(productos, fotos))
    
    return render_template('catalogo.html', productos_con_foto=productos_con_foto)

@app.route('/producto/<int:pid>')
def ruta_producto(pid):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (pid,))
    producto = cursor.fetchone()
    conn.close()
    
    if producto is None:
        return "Producto no encontrado", 404
    
    return render_template('producto.html', producto=producto)
  
if _name_ == '_main_':
    app.run(host='0.0.0.0', debug=True, port=5000)
    