from flask import Flask
from markupsafe import escape

app = Flask(__name__)

template_dir = "./templates"

# loads the template with given name from <template_dir>
def load_template(tname):
    with open( template_dir+'/'+tname+'.html') as tfile:
        return tfile.read()
    return "Cannot read template from file: templates/{tname}.html".format(tname=tname)

# test in browser: http://127.0.0.1:5000/
@app.route('/')
def index():
    return 'Hello world'

# test in browser: http://127.0.0.1:5000/kex
@app.route('/kex')
def kex():
    # this assumes the file <template_dir>/kex.html exists
    return load_template('kex')

# test in browser: http://127.0.0.1:5000/user/Victor
#   you  can change Victor into your own name.
@app.route('/user/<username>')
def hello_user(username):
    # this assumes the file <template_dir>/username.html exists
    return load_template('username').format(username=escape(username))

# test in browser: http://127.0.0.1:5000/user/Victor/kex
#   you can change Victor into your own name
#   and kex by your own favorite food.
@app.route('/user/<username>/<foodtype>')
def user_food(username, foodtype):
    # this assumes the file <template_dir>/username2.html exists
    return load_template('username2').format(username=escape(username),
                                             foodtype=escape(foodtype))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
