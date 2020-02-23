Webserver
=========

Du kan köra din egen (lokala) webserver med *Flask* och *Python*. Se också `FlaskPythonWebserver`_

1. Skapa en map *webapp*::

     $ mkdir webapp

2. Skapa en fil *app.py* med följande text ock spara filen i *webapp* mappen::

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
     
3. Öppna en terminal och går in i mappen *webapp*::

    $ cd webapp

4. Starta webservern::

     $ python app.py

   Ny lysnar din webserver till (lokala) *URL requests* på `http://127.0.0.1:5000`.
   
5. Öppna websidan i webbrowsern:

   Clicka här: `websidan`_ (dvs, http://127.0.0.1:5000/)

   Eller här: `kexsidan`_  (dvs, http://127.0.0.1:5000/kex)

6. Lägg till en link med `@app.route()`

   Nya linkar skapar man med `@app.route()`. Vi har redan skapat link
   ´/´ (med `@app.route('/')`) och '/kex' (med
   `app.route('/kex')`). Kopierar en av denna linkar och ändrar den i
   en ny link.

   Testar din nya link med webbrowsern.

7. Öppna websidan från en annan dator på samma nät

   Du kan öppna din websida från en annan dator om den är på samma
   nät. Först ska du ha namnet på datorn som kör webservern: i en
   *terminal*, ge kommandot::

     $ hostname

   Svaret är datorns namn. Till exempel, min dator hetar
   *too-ticki*. Om jag ge kommandot `hostname`, ser jag::

     $ hostname
     too-ticki

   På en annan dator (på samma nät), kann du användar det namn för att
   öppna en websida. I webbrowsern på den andra dator, skriv följande
   adressen: http://too-ticki.local:5000/ (bytt *too-ticki* för din dators
   namn).
   
   
.. _websidan:   http://127.0.0.1:5000/
.. _kexsidan:   http://127.0.0.1:5000/kex
.. _FlaskPythonWebserver: https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/2/



