from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'


@app.route('/kex')
def kex():
    return '''
    <!DOCTYPE=html>
    <html>
      <body>
         <h1>Kex Sidan</h1>
         <p>Kex är super gott!</p>
      </body>
    </html>
    '''

@app.route('/user/<username>')
def hello_user(username):
    return '''
    <!DOCTYPE=html>
    <html>
      <body>
         <h1>User</h1>
         <p>Hej, {uname}, tycker du om kex?</p>
      </body>
    </html>
    '''.format(uname=username)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
