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
    return render_template('aplicacion/recordatorios.html', recordatorios=recordatorios) #TODO

########################################################### RECORDATORIO ###########################################################

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

########################################################### MEDICAMENTO ###########################################################

@bp.route('/create',methods=['GET','POST'])
@login_require
def create_medicamento():
    if request.method=="POST":
        nombre = request.form['nombre_medicamento']
        description = request.form['descripcion_medicamento']
        dosis = request.form['dosis_medicamento']
        posologia = request.form['posologia_medicamento']
        precio = request.form['precio_medicamento']
        cantidad = request.form['cantidad_medicamento']

        error = None

        if not nombre_medicamento:
            error = 'Nombre del Medicamento requerido'
        if error is not None:
            flash(error)
        else:
            db,c = get_db()
            c.execute('insert into Medicamento (created_by,nombre,descripcion,dosis,posologia,precio,cantidad)'
                    ' values (%s,%s,%s,%s,%s)',(g.user['id'],,description,False))
        db.commit()
        return redirect(url_for('patrones.index')) #TODO

    return render_template('aplicacion/create.html') #TODO

##########################################################################################################################################
# Modificacion de medicamentos (requiere frontend)
@bp.route('/<int:id>/update',methods=['GET','POST'])
@login_require
def update_medicamento(id):
    medicamento = get_medicamento(id)
    if request.method == 'POST':
        dosis = request.form['dosis_medicamento']
        posologia = request.form['posologia_medicamento']
        precio = request.form['precio_medicamento']
        cantidad = request.form['cantidad_medicamento']

        error = None

        if error is not None:
            flash(error)
        else:
            db, c = get_db()
            c.execute('update Medicamento set dosis = %s, posologia = %s, precio = %s, cantidad = %s'
                ' where id = %s and created_by = %s', (dosis, posologia, precio, cantidad ,description, id, g.user['id']))
            db.commit()
            return redirect(url_for('patrones.index')) #TODO
    return render_template('aplicacion/update.html',medicamento=medicamento) #TODO

def get_medicamento(id):
    db,c = get_db()
    c.execute('select m.id, m.posologia, m.dosis, m.created_by, m.precio, m.cantidad' 
            ' u.username from Medicamento m join Usuario u on m.created_by = u.id where m.id = %s',(id,))
    medicamento = c.fetchone()
    if medicamento is None:
        abort(404,'El medicamento de id {0} no existe'.format(id))
    return medicamento

##########################################################################################################################################
# Eliminar de medicamentos (requiere frontend)
@bp.route('/<int:id>/delete',methods=['POST'])
@login_require
def delete_medicamento(id):
    db,c = get_db()
    c.execute('delete from Medicamento where id = %s and created_by = %s',(id,g.user['id']))
    db.commit()
    return redirect(url_for('patrones.index')) #TODO

########################################################### CITAS MEDICAS ###########################################################

# Creacion de citas medicas (requiere frontend)
@bp.route('/create',methods=['GET','POST'])
@login_require
def create_cita():
    if request.method=="POST":
        date = request.form['fecha_cita']
        doctor = request.form['doctor_cita']
        specialization = request.form['especialidad_cita']
        companion = request.form['acompanante_cita']

        error = None

        if not date:
            error = 'Fecha de la cita requerido'
        if error is not None:
            flash(error)
        else:
            db,c = get_db()
            c.execute('insert into Citas (created_by,date,doctor,specialization,companion)'
                    ' values (%s,%s,%s,%s,%s)',(g.user['id'],date,doctor,specialization,companion))
        db.commit()
        return redirect(url_for('patrones.index')) #TODO

    return render_template('aplicacion/create.html') #TODO
##########################################################################################################################################
# Modificacion de citas medicas (requiere frontend)
@bp.route('/<int:id>/update',methods=['GET','POST'])
@login_require
def update_cita(id):
    cita = get_cita(id)
    if request.method == 'POST':
        date = request.form['fecha_cita']
        doctor = request.form['doctor_cita']
        specialization = request.form['especialidad_cita']
        companion = request.form['acompanante_cita']
        error = None

        if error is not None:
            flash(error)
        else:
            db, c = get_db()
            c.execute('update Cita set date = %s, doctor = %s, specialization = %s, companion = %'
                ' where id = %s and created_by = %s', (date, doctor, specialization, companion, id, g.user['id']))
            db.commit()
            return redirect(url_for('patrones.index')) #TODO
    return render_template('aplicacion/update.html',cita=cita) #TODO

def get_cita(id):
    db,c = get_db()
    c.execute('select c.id, c.date, c.doctor, c.created_by, c.specialization, c.companion' 
            ' u.username from Cita c join Usuario u on c.created_by = u.id where c.id = %s',(id,))
    cita = c.fetchone()
    if cita is None:
        abort(404,'La cita de id {0} no existe'.format(id))
    return cita

##########################################################################################################################################
# Eliminar de medicamentos (requiere frontend)
@bp.route('/<int:id>/delete',methods=['POST'])
@login_require
def delete_cita(id):
    db,c = get_db()
    c.execute('delete from Cita where id = %s and created_by = %s',(id,g.user['id']))
    db.commit()
    return redirect(url_for('patrones.index')) #TODO
##########################################################################################################################################
@bp.route('/<string:pagina>')
@login_require
def interfaces(pagina):
    return render_template('aplicacion/{}.html'.format(pagina))