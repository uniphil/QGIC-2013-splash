from flask import render_template
from qgic13 import app


@app.route('/')
def home():
    return render_template('base.html', content='hello world!')
