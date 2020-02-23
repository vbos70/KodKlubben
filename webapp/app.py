from flask import Flask

app = Flask(__name__)

# test in browser: http://127.0.0.1:5000/
@app.route('/')
def index():
    return 'Hello world'

# test in browser: http://127.0.0.1:5000/kex
@app.route('/kex')
def kex():
    return 'KEX !!!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
