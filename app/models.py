from app.extensions import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ========== MODELO USUARIO (para autenticación) ==========
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<User {self.username}>'

# ========== MODELO MIEMBRO ==========
class Miembro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    
    tareas = db.relationship('Tarea', backref='miembro', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Miembro {self.nombre}>'

# ========== MODELO TAREA ==========
class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    completada = db.Column(db.Boolean, default=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    miembro_id = db.Column(db.Integer, db.ForeignKey('miembro.id'), nullable=True)
    
    def __repr__(self):
        return f'<Tarea {self.titulo}>'