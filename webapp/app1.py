from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/kex')
def kex():
    return 'KEX !!!'

@app.route('/user/<username>')
def hello_user(username):
    return "Hello {uname}!".format(uname=escape(username))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
