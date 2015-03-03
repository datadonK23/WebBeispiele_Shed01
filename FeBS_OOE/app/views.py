"""
Views
"""

from flask import render_template
from app import app
from app import connection
from models import get_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ref')
def ref():
    return render_template('ref.html')

# test page
@app.route('/test')
def test():
    document = get_data(connection)
    name = document["name"].encode()
    loc = document["loc"]["coordinates"]
    data = [name, loc]
    return render_template('ref.html', data=data)
