Webserver
=========

Du kan köra din egen (lokala) webserver med *Flask* och *Python*. Se också FlaskPytonWebserver_

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

   Clicka här: websidan_
   
.. websidan:   http://127.0.0.1:5000/
.. _FlaskPythonWebserver: https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/2/

