from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
app.config.from_pyfile('config.py')
from model import db, Sucursal, Paquete, Transporte  # Importa db y Sucursal desde model.py

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
        try:
            print(request.form)
            idsucursal = request.form.get('idsucursal')
            peso = request.form.get('peso')
            dirdestinatario = request.form.get('dirdestinatario')
            nomdestinatario = request.form.get('nomdestinatario')
            if not nomdestinatario:
                return redirect(url_for('funcion2'))
            entregado = request.form.get('entregado') == '1'  
            observaciones = request.form.get('observaciones')
            numeroenvio = random.randint(1000, 1500)
            idtransporte = request.form.get('idtransporte')  
            idrepartidor = request.form.get('idrepartidor')  
            
            idtransporte = int(idtransporte) if idtransporte else None
            idrepartidor = int(idrepartidor) if idrepartidor else None

            paquete = Paquete(
                numeroenvio=numeroenvio,
                peso=peso,
                nomdestinatario=nomdestinatario,
                dirdestinatario=dirdestinatario,
                entregado=entregado,
                observaciones=observaciones,
                idsucursal=idsucursal,
                idtransporte=idtransporte,
                idrepartidor=idrepartidor
            )
            db.session.add(paquete)
            db.session.commit()
            flash("Paquete guardado con éxito", "success")
        except Exception as e:
            db.session.rollback()
            flash("Error al guardar paquete", "error")
        return redirect(url_for('funcion1'))
    else:
        sucursales = Sucursal.query.order_by(Sucursal.id).all()
        return render_template('funcion2.html', sucursales=sucursales)

    
@app.route("/funcion3", methods=['GET', 'POST'])
def funcion3():
    if request.method == 'POST':
        try:
            paquete_ids = request.form.getlist('paquetes')
            id_sucursal = request.form.get('id_sucursal')
            if paquete_ids and id_sucursal:
                # Crear un nuevo transporte
                transporte = Transporte(
                    numerotransporte=random.randint(1000, 1500),
                    fechahorasalida=datetime.now(),
                    fechahorallegada=None,
                    idsucursal=id_sucursal
                )
                db.session.add(transporte)
                db.session.commit()
                
                # Asociar paquetes con el transporte
                for paquete_id in paquete_ids:
                    paquete = Paquete.query.get(paquete_id)
                    if paquete:
                        paquete.idtransporte = transporte.id
                        db.session.commit()
                flash("Paquetes asociados con el transporte correctamente", "success")
            else:
                flash("No se han seleccionado paquetes", "error")
            
            # Redirigir a funcion1 después de registrar el transporte
            return redirect(url_for('funcion1'))
        
        except Exception as e:
            db.session.rollback()
            flash("Error al guardar transporte", "error")
            return redirect(url_for('funcion3', sucursal=id_sucursal))
    
    elif request.method == 'GET':
        sucursal_id = request.args.get('sucursal')
        if not sucursal_id:
            flash("No se ha especificado la sucursal", "error")
            return redirect(url_for('funcion1'))
        
        # Obtener paquetes que no están entregados y no tienen repartidor asignado
        paquetes = Paquete.query.filter_by(entregado='0', idrepartidor=None).all()
        
        # Verificar si se encontraron paquetes
        if not paquetes:
            flash("No hay paquetes pendientes", "error")
            print("No hay paquetes pendientes")
        else:
            print(f"Paquetes encontrados: {len(paquetes)}")
        
        return render_template('funcion3.html', paquetes=paquetes, id_sucursal=sucursal_id)
    
    
@app.route("/funcion4", methods=['GET', 'POST'])
def funcion4():
    if request.method == 'POST':
        try:
            transporte_id = request.form.get('transporte_id')
            transporte = Transporte.query.get(transporte_id)
            if transporte and not transporte.fechahorallegada:
                transporte.fechahorallegada = datetime.now()
                db.session.commit()
                flash("Llegada del transporte registrada con éxito", "success")
            else:
                flash("Transporte no válido o ya registrado", "error")
        except Exception as e:
            db.session.rollback()
            flash("Error al registrar llegada del transporte", "error")
        return redirect(url_for('funcion1'))
    
    elif request.method == 'GET':
        sucursal_id = request.args.get('sucursal')
        if not sucursal_id:
            flash("No se ha especificado la sucursal", "error")
            return redirect(url_for('funcion1'))

        transportes = Transporte.query.filter_by(idsucursal=sucursal_id, fechahorallegada=None).all()
        
        if not transportes:
            flash("No hay transportes pendientes de llegada", "error")
        
        return render_template('funcion4.html', transportes=transportes)




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
