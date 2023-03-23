from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import InputForm
from app.models import Input
import datetime

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm()
    if form.validate_on_submit():
        input_text = form.input_text.data
        input_time = datetime.datetime.now()
        new_input = Input(text=input_text, time=input_time)
        db.session.add(new_input)
        db.session.commit()
        flash('Input submitted successfully.')
        return redirect(url_for('index'))
    inputs = Input.query.order_by(Input.time.desc()).all()
    return render_template('index.html', form=form, inputs=inputs)
