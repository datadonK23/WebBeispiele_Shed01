"""
Views
"""

from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/challenge')
def challenge():
    return render_template('challenge.html')

@app.route('/tracks')
def tracks():
    return render_template('tracks.html')
  
@app.route('/statistics')
def statistics():
    return render_template('statistics.html')

@app.route('/routing')
def routing():
    return render_template('routing.html')

