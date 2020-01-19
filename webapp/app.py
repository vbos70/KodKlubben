from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/kex')
def kex():
    return 'KEX !!!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
