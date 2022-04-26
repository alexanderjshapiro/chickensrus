from app import chickensrus
from flask import render_template


@chickensrus.route('/')
def home():
    return render_template('index.html')
