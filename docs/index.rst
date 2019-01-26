.. Kodklubben documentation master file, created by
   sphinx-quickstart on Sat Jan 26 12:30:09 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Välkommen till Kodklubben's dokumentation
=========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Innehehåll
==========

* :ref:`genindex`
* :ref:`search`


Pong
====

Spelet *Pong* finns i mappen *./pgzero/pong* i Kodklubbens repository
(för att ladda ner eller klona den, ser `Kodklubben GitHub`_).

Spelet startas i terminalen med kommandot::

  $ pgzrun pong.py

Obs: kommandot funkar om du är i mappen 'pgzero/pong' (man kommer dit
med kommandot ``cd pgzero/pong``).

*Pong* ser ut som här:

.. image:: images/pong0.png

Efter 3 sekunder börjar bollen röra sig mot vänster spelaren. Vänster
spelaren kann flyttas upp med ``w``-knappen och ner med ``z``-knappen.

När bollens vänstra sidan rör (vänstra) spelarens högra sidan, blir
bollen slagen tillbaka till högra spelaren.

Om du väntar tills bollen kommer nära den högra spelaren, märker du
att högra spelaren kann inte röra sig och att bollen går rakt igenom
den! Det är inte bra. Programmet *pong.py* har fel ('bugs').  Kan du
fixa denna ´bugs'?

Röra högra spelaren
-------------------

1. Öppna *pong.py* i din textredigerara ('text editor'), t.ex *Thonny
   IDE* eller *Idle*.

2. Letar efter den här kodlinjer i *pong.py*::
     
        # Player1
        if keyboard.w:
            # 'w' means UP
            player1.speed_y = -SPEED
        elif keyboard.z:
            # 'z' means DOWN
            player1.speed_y = SPEED
        else:
            # otherwise no movement
            player1.speed_y = 0

	# Player2
        if keyboard.i:
            # 'i' means UP
            # remove 'pass' and write the code here
            pass
        elif keyboard.m:
            # 'm' means DOWN
            # remove 'pass' and write the code here
            pass
        else:
            # otherwise no movement
            player2.speed_y = 0

3. Läs kodlinjerna. Det finns instruktioner var du ska ändra dom och
   genom att kålla linjerna for vänstra spelaren (``player1``) kan du
   skriva kodlinjer som får högra spelaren att röra sig upp med
   ``i``-knappen och ner med ``m`` knappen.

   Kodlinjerna som ska ändras har nu ordet ``pass``.



.. _Kodklubben GitHub: https://github.com/vbos70/KodKlubben/

