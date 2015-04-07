"""
Views
"""

from flask import render_template
from flask import request
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/challenge')
def challenge():
    return render_template('challenge.html')

@app.route('/tracks')
def tracks():
    track_name = None #"Auffahrt A  Garsten"
    return render_template('tracks.html', track_selected=track_name)

@app.route('/routing')
def routing():
    route_waypoints = None #["C", "X", "H", "F", "X", "I", "D", "X", "F", "H", "X", "D", "I", "X", "G", "E", "X", "B", "A", "X", "E", "G", "X", "C", "B", "X", "S"]
    return render_template('routing.html', waypoints=route_waypoints)

@app.route('/rollofhonor')
def rollofhonor():
    return render_template('rollofhonor.html')
 
"""
@app.route('/tracksel/<track>', methods=['POST'])
def tracksel(track=None):
    track = request.form["trackSelected"]
    return track
 """