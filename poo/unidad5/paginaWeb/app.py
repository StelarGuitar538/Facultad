from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')
from model import db, Sucursal  # Importa db y Sucursal desde model.py

# Inicializa SQLAlchemy con la aplicación Flask
#db.init_app(app)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def index():
    role = request.form.get('role')
    if role == 'despachante':
        return redirect(url_for('funcion1'))
    elif role == 'repartidor':
        return render_template('repartidor.html')

@app.route("/funcion1")
def funcion1():
    sucursales = Sucursal.query.order_by(Sucursal.numero).all()
    return render_template('funcion1.html', sucursales=sucursales)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
