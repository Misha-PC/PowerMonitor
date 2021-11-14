import flask
from app import app


def event_stream():
    for message in ['message one', 'message two']:
        print (message)
        yield 'data: %s\n\n' % message


@app.route('/stream')
def stream():
    return flask.Response(event_stream(), mimetype="text/event-stream")
