from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import Miembro, Tarea

def register_routes(app):
    
    @app.route('/')
    @login_required
    def home():
        miembros = Miembro.query.all()
        tareas = Tarea.query.all()
        return render_template('home.html', miembros=miembros, tareas=tareas)

    # ========== CRUD MIEMBROS ==========
    @app.route('/miembro/agregar', methods=['POST'])
    @login_required
    def agregar_miembro():
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        
        if nombre and email:
            miembro = Miembro(nombre=nombre, email=email)
            db.session.add(miembro)
            db.session.commit()
            flash('Miembro agregado', 'success')
        
        return redirect(url_for('home'))

    @app.route('/miembro/editar/<int:id>', methods=['POST'])
    @login_required
    def editar_miembro(id):
        miembro = Miembro.query.get_or_404(id)
        miembro.nombre = request.form.get('nombre')
        miembro.email = request.form.get('email')
        db.session.commit()
        flash('Miembro editado', 'success')
        return redirect(url_for('home'))

    @app.route('/miembro/eliminar/<int:id>')
    @login_required
    def eliminar_miembro(id):
        miembro = Miembro.query.get_or_404(id)
        db.session.delete(miembro)
        db.session.commit()
        flash('Miembro eliminado', 'success')
        return redirect(url_for('home'))

    # ========== CRUD TAREAS ==========
    @app.route('/tarea/agregar', methods=['POST'])
    @login_required
    def agregar_tarea():
        titulo = request.form.get('titulo')
        descripcion = request.form.get('descripcion')
        miembro_id = request.form.get('miembro_id')
        
        if titulo:
            tarea = Tarea(titulo=titulo, descripcion=descripcion, miembro_id=miembro_id if miembro_id else None)
            db.session.add(tarea)
            db.session.commit()
            flash('Tarea agregada', 'success')
        
        return redirect(url_for('home'))

    @app.route('/tarea/completar/<int:id>')
    @login_required
    def completar_tarea(id):
        tarea = Tarea.query.get_or_404(id)
        tarea.completada = not tarea.completada
        db.session.commit()
        flash('Estado de tarea actualizado', 'success')
        return redirect(url_for('home'))

    @app.route('/tarea/editar/<int:id>', methods=['POST'])
    @login_required
    def editar_tarea(id):
        tarea = Tarea.query.get_or_404(id)
        tarea.titulo = request.form.get('titulo')
        tarea.descripcion = request.form.get('descripcion')
        tarea.miembro_id = request.form.get('miembro_id') if request.form.get('miembro_id') else None
        db.session.commit()
        flash('Tarea editada', 'success')
        return redirect(url_for('home'))

    @app.route('/tarea/eliminar/<int:id>')
    @login_required
    def eliminar_tarea(id):
        tarea = Tarea.query.get_or_404(id)
        db.session.delete(tarea)
        db.session.commit()
        flash('Tarea eliminada', 'success')
        return redirect(url_for('home'))