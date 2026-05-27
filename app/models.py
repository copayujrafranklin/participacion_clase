from app import db
from datetime import datetime

class Miembro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    
    tareas = db.relationship('Tarea', backref='miembro', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Miembro {self.nombre}>'

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    completada = db.Column(db.Boolean, default=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    miembro_id = db.Column(db.Integer, db.ForeignKey('miembro.id'), nullable=True)
    
    def __repr__(self):
        return f'<Tarea {self.titulo}>'