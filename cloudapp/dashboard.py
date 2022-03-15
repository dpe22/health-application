from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from cloudapp.auth import login_required
from cloudapp.db import get_db

bp = Blueprint('dashboard', __name__)

@bp.route('/')
def index():
    db = get_db()
    devices = db.execute(
        'SELECT d.id, firstname, lastname, u.created, d.created, device_name, username, measurement, units, patient_id'
        ' FROM device d JOIN user u ON d.patient_id = u.id'
        ' ORDER BY d.created DESC'
    ).fetchall()
    return render_template('dashboard/index.html', devices=devices)

# Add Device
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        device_name = request.form['device_name']
        measurement = request.form['measurement']
        units = request.form['units']
        patient_id = request.form['patient_id']
        error = None

        if not device_name:
            error = 'Device name is required.'
        if not measurement:
            error = 'Measurement value is required.'
        if not units:
            error = 'Please describe units of measurement.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO device (device_name, measurement, units, patient_id) VALUES (?, ?, ?, ?)",
                (device_name, measurement, units, patient_id),
            )
            db.commit()
            return redirect(url_for('dashboard.index'))

    return render_template('dashboard/create.html')

# UPDATE Device
def get_device(id, check_patient=True):
    post = get_db().execute(
        'SELECT d.id, firstname, lastname, u.created, device_name, username, measurement, units, patient_id, username'
        ' FROM device d JOIN user u ON d.patient_id = u.id'
        ' WHERE d.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Device id {id} doesn't exist.")

    if check_patient and post['patient_id'] != g.user['id']:
        abort(403)

    return post

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    device = get_device(id)

    if request.method == 'POST':
        device_name = request.form['device_name']
        measurement = request.form['measurement']
        units = request.form['units']
        error = None

        if not device_name:
            error = 'Device name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE device SET device_name = ?, measurement = ?, units = ?'
                ' WHERE id = ?',
                (device_name, measurement, units, id)
            )
            db.commit()
            return redirect(url_for('dashboard.index'))

    return render_template('dashboard/update.html', device=device)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_device(id)
    db = get_db()
    db.execute('DELETE FROM device WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('dashboard.index'))