from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello():
    return "hello world"

@app.route('/test')
def test_route():
    return "in / test yo"

app.run()
# serve(app)
