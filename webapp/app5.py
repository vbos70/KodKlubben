from flask import Flask
from markupsafe import escape

# import the page functions:
from app5_kex import kex_page
from app5_user import user_page
from app5_user2 import user2_page


app = Flask(__name__)

# test in browser: http://127.0.0.1:5000/
@app.route('/')
def index():
    return 'Hello world'

# test in browser: http://127.0.0.1:5000/kex
@app.route('/kex')
def kex():
    return kex_page()

# test in browser: http://127.0.0.1:5000/user/Victor
#   you  can change Victor into your own name.
@app.route('/user/<username>')
def hello_user(username):
    return user_page(escape(username))

# test in browser: http://127.0.0.1:5000/user/Victor/kex
#   you can change Victor into your own name
#   and kex by your own favorite food.
@app.route('/user/<username>/<foodtype>')
def user_food(username, foodtype):
    return user2_page(escape(username), escape(foodtype))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
