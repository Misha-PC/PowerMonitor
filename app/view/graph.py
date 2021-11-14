from flask import render_template
from app import app


@app.route('/graph')
def draw_graph():
    return render_template("graph.html")
