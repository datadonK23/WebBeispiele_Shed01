"""
Views
"""

from flask import render_template
from app import app
from app import connection
#from models import get_data
from models import Features

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ref')
def ref():
    return render_template('ref.html')

# test page
@app.route('/test')
def test():
    features = Features(connection)
    documents = features.get_unbekannt()
    namelist = []
    for document in documents:
        name = document["name"]
        namelist.append(name)
    return render_template('ref.html', data=namelist)
