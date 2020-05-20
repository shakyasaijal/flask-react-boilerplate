import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# App Configuration
if app.config['ENV'] == "production":
    app.config.from_object('config.config.ProductionConfig')
elif app.config['ENV'] == "testing":
    app.config.from_object('config.config.TestingConfig')
else:   
    app.config.from_object('config.config.DevelopmentConfig')

# Database Configuration
'''
SQLite3
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://saijal:saijal@localhost/flaskreact'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from flaskreact import routes
