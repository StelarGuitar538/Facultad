from __main__ import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

class Sucursal(db.Model):
    __tablename__ = 'sucursal'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)
    provincia = db.Column(db.String(30))
    localidad = db.Column(db.String(30))
    direccion = db.Column(db.String(60))

class Repartidor(db.Model):
    __tablename__ = 'repartidor'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)
    nombre = db.Column(db.String(60))
    dni = db.Column(db.String(8))
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))

class Paquete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numeroenvio = db.Column(db.Integer, unique=True, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    nomdestinatario = db.Column(db.String(80), nullable=False)
    dirdestinatario = db.Column(db.String(120), nullable=False)
    entregado = db.Column(db.Boolean, nullable=False, default=False)
    observaciones = db.Column(db.String(200))
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    idtransporte = db.Column(db.Integer, db.ForeignKey('transporte.id'), nullable=True)
    idrepartidor = db.Column(db.Integer, db.ForeignKey('repartidor.id'), nullable=True)


class Transporte(db.Model):
    __tablename__ = 'transporte'
    id = db.Column(db.Integer, primary_key=True)
    numerotransporte = db.Column(db.Integer)
    fechahorasalida = db.Column(db.DateTime)
    fechahorallegada = db.Column(db.DateTime)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
