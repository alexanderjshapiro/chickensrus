from flask import Flask

chickensrus = Flask(__name__)

from app import routes
