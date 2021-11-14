from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    # return "Index page"
    return render_template('index.html')
