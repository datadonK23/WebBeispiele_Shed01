"""
Views
"""

from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ref')
def ref():
    return render_template('ref.html')
