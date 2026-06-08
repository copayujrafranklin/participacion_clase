from flask import Flask
from config import Config
from app.extensions import db, bcrypt, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializar extensiones
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    # Importar modelos (para que Flask-Migrate los detecte)
    from app.models import Miembro, Tarea, User
    
    # Crear tablas si no existen (solo para desarrollo)
    with app.app_context():
        db.create_all()
    
    # Registrar blueprint de autenticación
    from app.auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    # Registrar rutas principales (miembros/tareas)
    from app.routes import register_routes
    register_routes(app)
    
    return app