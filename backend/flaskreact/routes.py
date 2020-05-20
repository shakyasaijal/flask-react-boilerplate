from flask import request, render_template
from flaskreact import app
from flaskreact.models.users import User

@app.route('/')
def index():
    return render_template("index.html")

