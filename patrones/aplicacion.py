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

    c.execute('select m.id, m.description, u.username, m.medicine, m.posology, m.amount from Medicamento m JOIN Usuario u on '
            'm.created_by = u.id where m.created_by=%s',(g.user['id'],))
    medicamentos = c.fetchall()

    c.execute('select c.id, c.specialization, u.username, c.date, c.doctor, c.companion from Cita c JOIN Usuario u on '
            'c.created_by = u.id where c.created_by=%s',(g.user['id'],))
    citas = c.fetchall()

    #c.execute('select r.id, r.description, u.username, r.completed, r.created_at from Recordatorio r JOIN Usuario u on '
    #        'r.created_by = u.id where r.created_by=%s order by created_at desc',(g.user['id'],))
    #recordatorios = c.fetchall()
    return render_template('aplicacion/recordatorios.html', recordatorios=recordatorios, medicamentos=medicamentos, citas=citas) 

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

@bp.route('/createM',methods=['GET','POST'])
@login_require
def createM():
    if request.method=="POST":
        nombre = request.form['nombre_medicamento']
        description = request.form['descripcion_medicamento']
        dosis = request.form['dosis_medicamento']
        posologia = request.form['posologia_medicamento']
        precio = request.form['precio_medicamento']
        cantidad = request.form['cantidad_medicamento']

        error = None

        if not nombre:
            error = 'Nombre del Medicamento requerido'
        if error is not None:
            flash(error)
        else:
            db,c = get_db()
            c.execute('insert into Medicamento (created_by,medicine,description,dose,posology,price,amount)'
                    ' values (%s,%s,%s,%s,%s,%s,%s)',(g.user['id'], nombre, description, dosis, posologia, precio, cantidad))
        db.commit()
        return redirect(url_for('patrones.index'))

    return render_template('aplicacion/createM.html')

##########################################################################################################################################
# Modificacion de medicamentos (requiere frontend)
@bp.route('/<int:id>/updateM',methods=['GET','POST'])
@login_require
def updateM(id):
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
            c.execute('update Medicamento set dose = %s, posology = %s, price = %s, amount = %s'
                ' where id = %s and created_by = %s', (dosis, posologia, precio, cantidad, id, g.user['id']))
            db.commit()
            return redirect(url_for('patrones.index')) 
    return render_template('aplicacion/updateM.html',medicamento=medicamento) 

def get_medicamento(id):
    db,c = get_db()
    c.execute('select m.id, m.posology, m.dose, m.created_by, m.price, m.amount,' 
            ' u.username from Medicamento m join Usuario u on m.created_by = u.id where m.id = %s',(id,))
    medicamento = c.fetchone()
    if medicamento is None:
        abort(404,'El medicamento de id {0} no existe'.format(id))
    return medicamento

##########################################################################################################################################
# Eliminar de medicamentos (requiere frontend)
@bp.route('/<int:id>/deleteM',methods=['POST'])
@login_require
def deleteM(id):
    db,c = get_db()
    c.execute('delete from Medicamento where id = %s and created_by = %s',(id,g.user['id']))
    db.commit()
    return redirect(url_for('patrones.index')) 

########################################################### CITAS MEDICAS ###########################################################

# Creacion de citas medicas (requiere frontend)
@bp.route('/createC',methods=['GET','POST'])
@login_require
def createC():
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
            c.execute('insert into Cita (created_by,date,doctor,specialization,companion)'
                    ' values (%s,%s,%s,%s,%s)',(g.user['id'],date,doctor,specialization,companion))
        db.commit()
        return redirect(url_for('patrones.index')) 

    return render_template('aplicacion/createC.html') 
##########################################################################################################################################
# Modificacion de citas medicas (requiere frontend)
@bp.route('/<int:id>/updateC',methods=['GET','POST'])
@login_require
def updateC(id):
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
            return redirect(url_for('patrones.index')) 
    return render_template('aplicacion/updateC.html',cita=cita) 

def get_cita(id):
    db,c = get_db()
    c.execute('select c.id, c.date, c.doctor, c.created_by, c.specialization, c.companion,' 
            ' u.username from Cita c join Usuario u on c.created_by = u.id where c.id = %s',(id,))
    cita = c.fetchone()
    if cita is None:
        abort(404,'La cita de id {0} no existe'.format(id))
    return cita

##########################################################################################################################################
# Eliminar de medicamentos (requiere frontend)
@bp.route('/<int:id>/deleteC',methods=['POST'])
@login_require
def deleteC(id):
    db,c = get_db()
    c.execute('delete from Cita where id = %s and created_by = %s',(id,g.user['id']))
    db.commit()
    return redirect(url_for('patrones.index')) 
##########################################################################################################################################
@bp.route('/<string:pagina>')
@login_require
def interfaces(pagina):
    return render_template('aplicacion/{}.html'.format(pagina))