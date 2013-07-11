from flask import render_template, url_for, redirect
from qgic13 import app


@app.route('/')
def home():
    return redirect(url_for('splash'))
    # return "/splash", 302
    #return render_template('base.html', content='hello world!')


@app.route('/splash')
def splash():
    return render_template('splash.html')


@app.route('/element-test')
def el_test():
    return render_template('element-test.html')
