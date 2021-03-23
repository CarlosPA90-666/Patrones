from flask import (Blueprint, flash, g, render_template, request, url_for, redirect)
from werkzeug.exceptions import abort
from patrones.auth import login_require
from patrones.db import get_db

bp = Blueprint('patrones',__name__)

@bp.route('/')
@login_require
def index():
    db,c = get_db()
    c.execute('select r.id, r.description, u.username, r.completed, r.created_at from Recordatorio r JOIN Usuario u on '
            'r.created_by = u.id where r.created_by=%s order by created_at desc',(g.user['id'],))
    recordatorios = c.fetchall()
    return render_template('aplicacion/recordatorios.html', recordatorios=recordatorios)

@bp.route('/create',methods=['GET','POST'])
@login_require
def create():
    if request.method=="POST":
        description = request.form['description']
        error = None

        if not description:
            error = 'Descripcion es requerida'
        if error is not None:
            flash(error)
        else:
            db,c = get_db()
            c.execute('insert into Recordatorio (created_by,description,completed)'
                    ' values (%s,%s,%s)',(g.user['id'],description,False))
        db.commit()
        return redirect(url_for('patrones.index'))

    return render_template('aplicacion/create.html')

def get_recordatorio(id):
    db,c = get_db()
    c.execute('select r.id, r.description, r.completed, r.created_by, r.created_at,' 
            ' u.username from Recordatorio r join Usuario u on r.created_by = u.id where r.id = %s',(id,))
    recordatorio = c.fetchone()
    if recordatorio is None:
        abort(404,'El todo de id {0} no existe'.format(id))
    return recordatorio

@bp.route('/<int:id>/update',methods=['GET','POST'])
@login_require
def update(id):
    recordatorio = get_recordatorio(id)
    if request.method == 'POST':
        description = request.form['description']
        error = None

        if error is not None:
            flash(error)
        else:
            db, c = get_db()
            c.execute('update Recordatorio set description = %s where id = %s and created_by = %s', (description, id, g.user['id']))
            db.commit()
            return redirect(url_for('patrones.index'))
    return render_template('aplicacion/update.html',recordatorio=recordatorio)

@bp.route('/<int:id>/delete',methods=['POST'])
@login_require
def delete(id):
    db,c = get_db()
    c.execute('delete from recordatorio where id = %s and created_by = %s',(id,g.user['id']))
    db.commit()
    return redirect(url_for('patrones.index'))

@bp.route('/<int:id>/complete',methods=['GET','POST'])
@login_require
def complete(id):
    recordatorio = get_recordatorio(id)
    if request.method == 'POST':
        completed = True if request.form.get('completed') == 'on' else False
        error = None

        if error is not None:
            flash(error)
        else:
            db, c = get_db()
            c.execute('update recordatorio set completed = %s where id = %s and created_by = %s', (completed,id, g.user['id']))
            db.commit()
            return redirect(url_for('patrones.index'))
    return render_template('aplicacion/complete.html',recordatorio=recordatorio)

@bp.route('/<string:pagina>')
@login_require
def interfaces(pagina):
    return render_template('aplicacion/{}.html'.format(pagina))