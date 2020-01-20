Webserver
=========

Du kan köra din egen (lokala) webserver med *Flask* och *Python*. Se också `FlaskPythonWebserver`_

1. Skapa en map *webapp*::

     $ mkdir webapp

2. Skapa en fil *app.py" med följande text ock spara filen i *webapp* mappen::

    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello world'

    @app.route('/kex')
    def kex():
        return 'KEX !!!'

    if __name__ == '__main__':
     
3. Öppna en terminal och går in i mappen *webapp*::

    $ cd webapp

4. Starta webservern::

     $ python app.py

5. Öppna websidan i webbrowsern:

   Clicka här: `websidan`_ (http://127.0.0.1:5000/)

   Eller här: `kexsidan`_  (http://127.0.0.1:5000/kex)

6. Lägg till en link med `@app.route()`

   Nya linkar skapar man med `@app.route()`. Vi har redan skapat link
   ´/´ (med `@app.route('/')`) och '/kex' (med
   `app.route('/kex')`). Kopierar en av denna linkar och ändrar den i
   en ny link.
   
.. _websidan:   http://127.0.0.1:5000/
.. _kexsidan:   http://127.0.0.1:5000/kex
.. _FlaskPythonWebserver: https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/2/



