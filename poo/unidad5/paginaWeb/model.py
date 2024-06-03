from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class sucursal(db.Model):
    __tablename__ = 'sucursal'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)
    provincia = db.Column(db.String(20))
    localidad = db.Column(db.String(20))
    direccion = db.Column(db.String(200))
    
class repartidor(db.Model):
    __tablename__ = 'repartidor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    dni = db.Column(db.Integer)
    
class paquete(db.Model):
    __tablename__ = 'paquete'
    id = db.Column(db.Integer, primary_key=True)
    numeroEnvio = db.Column(db.Integer)
    peso = db.Column(db.Integer)
    nombreDestinatario = db.Column(db.String(20))
    direccionDestinatario = db.Column(db.String(200))
    entregado = db.Column(db.Boolean)
    observaciones = db.Column(db.String(200))
    repartidor = db.Column(db.Integer, db.ForeignKey('repartidor.id'))
    sucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    
class transporte(db.Model):
    __tablename__ = 'transporte'
    id = db.Column(db.Integer, primary_key=True)
    numeroTransporte = db.Column(db.Integer)
    fechaHoraSaida = db.Column(db.DateTime)
    fechaHoraLLegada = db.Column(db.DateTime)