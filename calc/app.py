from operations import ops
from flask import Flask, request

app = Flask(__name__)


@app.route('/math/<op>')
def math(op):
    return str(ops[op](float(request.args['a']), float(request.args['b'])))


