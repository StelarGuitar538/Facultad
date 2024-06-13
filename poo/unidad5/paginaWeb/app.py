from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random


app = Flask(__name__)
app.config.from_pyfile('config.py')
from model import db, Sucursal, Paquete  # Importa db y Sucursal desde model.py

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

@app.route("/funcion2", methods=['GET', 'POST'])
def funcion2():
    if request.method == 'POST':
        print(request.form)
        idsucursal = request.form.get('idsucursal')
        peso = request.form.get('peso')
        dirdestinatario = request.form.get('dirdestinatario')
        nomdestinatario = request.form.get('nomdestinatario')
        if not nomdestinatario:
            return redirect(url_for('funcion2'))
        entregado = 'entregado' in request.form #true si el usuario seleccionó entregado
        observaciones = request.form.get('observaciones')
        numeroenvio = random.randint(1000, 1500)
        idtransporte = request.form.get('idTransporte')
        idrepartidor = request.form.get('idRepartidor')
        paquete = Paquete(numeroenvio = numeroenvio, peso = peso, nomdestinatario = nomdestinatario, dirdestinatario = dirdestinatario, entregado = entregado, observaciones = observaciones, idsucursal = idsucursal, idtransporte = idtransporte, idrepartidor = idrepartidor)
        db.session.add(paquete)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        sucursales = Sucursal.query.order_by(Sucursal.id).all()
        return render_template('funcion2.html', sucursales=sucursales)
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
