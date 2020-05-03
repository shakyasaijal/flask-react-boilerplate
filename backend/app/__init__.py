from flask import Flask

app = Flask(__name__)

# App Configuration
if app.config['ENV'] == "production":
    app.config.from_object('config.config.ProductionConfig')
elif app.config['ENV'] == "testing":
    app.config.from_object('config.config.TestingConfig')
else:   
    app.config.from_object('config.config.DevelopmentConfig')

from app import routes