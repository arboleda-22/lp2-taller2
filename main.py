from flask import Flask, render_template, redirect
import sqlite3

app = Flask(__name__)

def obtener_productos():
    conexion = sqlite3.connect("productos.db")  # <-- usa la misma BD que crear_db.py
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos;")
    productos = [dict(p) for p in cursor.fetchall()]
    conexion.close()
    return productos

@app.route("/")
def ruta_raiz():
    productos = obtener_productos()  # <-- consulta cada vez que entras
    return render_template("index.html", productos=productos)

@app.route("/catalogo")
def ruta_catalogo():
    conexion = sqlite3.connect("productos.db")
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos;")
    productos = [dict(p) for p in cursor.fetchall()]
    conexion.close()
    
    # Agrega el nombre de la foto basado en el id
    productos_con_foto = []
    for p in productos:
        foto = f"{p['id']}.jpg"  # 101.jpg, 104.jpg, etc
        productos_con_foto.append((p, foto))
    
    return render_template("catalogo.html", productos_con_foto=productos_con_foto)

@app.route("/producto/<int:pid>")
def ruta_producto(pid):
    productos = obtener_productos()
    for producto in productos:
        if pid == producto["id"]:
            return render_template("producto.html", producto=producto)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
