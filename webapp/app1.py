from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# test in browser: http://127.0.0.1:5000/
@app.route('/')
def index():
    return 'Hello world'

# test in browser: http://127.0.0.1:5000/kex
@app.route('/kex')
def kex():
    return 'KEX !!!'

# test in browser: http://127.0.0.1:5000/user/Victor
#   You can change Victor into your own name.
@app.route('/user/<username>')
def hello_user(username):
    return "Hello {uname}!".format(uname=escape(username))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
