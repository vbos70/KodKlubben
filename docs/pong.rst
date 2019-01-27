Pong
====

*Pong* är en gammaldags datorspel som jag spelada först i 1978 eller
till och med tidigare. Spelet har två rektanglar som spelarna och en
cirkel som bollen. Varje spelare försöker att slå bollen utanför
fältet längs den andra spelare.

Vår *Pong* spel ser ut som här:

.. image:: images/pong0.png

Spelarna är på var sin sida av fältet och dom kan flytta upp och ner
men inte till vänster eller höger. Bollen rör sig mellan spelarna. En
spelare slår bollen tillbaka genom att placera hans rektangel framför
bollen. Om en spelara slår bollen med övre delen av hans rektangel, så
går bollen lite mera uppåt. Om spelaren däremot slår bollen med nedre
delen av hans rekangle, så går bollen lite mera neråt.

Kod för Pong
------------

Spelet *Pong*'s kod finns i mappen *./pgzero/pong* i Kodklubbens
repository (för att ladda ner eller klona den, ser `Kodklubben
GitHub`_).

.. _Kodklubben GitHub: https://github.com/vbos70/KodKlubben/

Spelet startas i terminalen med kommandot::

  $ pgzrun pong.py

Obs: kommandot funkar om du är i mappen 'pgzero/pong'. Man kommer dit
med kommandot ``cd pgzero/pong``. Se :doc:pong för mera kommandon.

Efter 3 sekunder börjar bollen röra sig mot den vänstra spelaren. Vänstra
spelaren kann flyttas upp med ``w``-knappen och ner med ``z``-knappen.

När bollens vänstra sidan rör (vänstra) spelarens högra sidan, blir
bollen slagen tillbaka till den högra spelaren.

Om du väntar nu tills bollen kommer nära den högra spelaren, märker du
att den kann inte röra sig och att bollen går till och med rakt igenom
den högra spelaren! Det är inte bra. Programmet *pong.py* har fel
('bugs').  Kan du fixa denna 'bugs'?

Koordinater
-----------

*Pong* är en 2-dimensional spel. Vi har alltså horisontala koordinater
och vertikala koordinater. Horisontala koordinater kallas också för
*X-koordinater* och vertikala koordinater kallas för
*Y-koordinater*. En punkt på skärmen har en X-koordinat och en
Y-koordinat. Vi skriver punktens koordinater som *(X, Y)*.

På en dator skärm börjar X och Y-koordinater vanligtvis i vänstra topp
hörnan. Dvs, punkten med koordinater (0,0) är skärmens vänstra topp
hörnan.

När man gär till höger blir X-koordinaten större. När man går ner blir
Y-koordinaten större. Därfor har skärmens högra botten hörnan
största koordinaterna.
 
Om skärmens storlek är 800x600 *pixlar*, har den 800 horisontala
pixlar och 600 vertikala pixlar. Koordinater börjar räknas
från 0. Därför, en skärm med storlek 800x600 har X-koordinater från
0..799 och Y-koordinater från 0..599. Obs., X-koordinaten 800 finns
inte på skärmen och Y-koordinaten 600 inte heller. Skärmens högra
botten hörna har koordinater (799, 599).

Nästa bild visar det här koordinat systemet för en skärm med storlek
*WxH*. Du ser (och förstår?!) att högra botten hörna har koordinater
(W-1, H-1) och inte (W, H).

.. image:: images/pong_coords.png
	   

Spelets aktörer
---------------

*Pong* har 3 *aktörer*:

1. Vänstra spelaren;

2. Högra spelaren;

3. Bollen.

Aktörernas position och hastighet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aktörerna har an position som vi indikerar med en X och Y-koordinater,
t.ex. (0,0) och (50, 211). Aktörerna har också en
*hastighet*. Hastigheten ändrar en aktörs position från ett ögonblick
till ett annat. I *Pong* har hastigheten en *X-riktning* och en
*Y-riktning*. X-riktningen ändrar en aktörs X-koordinat och
Y-riktningen ändrar en aktörs Y-koordinat. När hastighetens X-riktning
(eller Y-riktning) är 0, ändrar aktörens X-koordinat (eller
Y-koordinat) inte.
  
Spelarna går bara upp och ner. När en spelare går uppåt, blir hans
Y-koordinat mindre: hans hastighet är *negativ*. När en spelare går
neråt, blir hans Y-koordinat större: hans hastighet är positiv.

Programmets 'main loop'
-----------------------

Datorspel har ett visst antal steg som körs om och om och om tills
spelet är slut. Denna steg ar spelets 'main loop'. En 'main loop'
beräknar först hur spelets aktörerna påverka varandra och vad deras
nya positioner är. Sedan uppdaterar 'main loop'-en skärmen enligt
denna nya positioner. Till slut, kållar 'main loop'-en om spelet är
slut eller om dessa steg ska utföras på nytt.

*Pong* programmet gör följande steg mycket snabbt (minst 20 gånger per
 sekund!):
 
1. Ändrar spelarnas hastighet beroende på tangenterna som trycks in.

2. Ändrar spelarnas position beroende på deras hastighet.
   
3. Ändrar bollens position beroende på denns hastighet (båda i X och Y-riktning).

4. Om en spelare slår bollen, ändrar bollens hastighet.

5. Om bollen rör på toppen av fältet, ändrar dess Y-riktning neråt.

6. Om bollen rör på botten av fältet, ändrar dess Y-riktning uppåt.

7. Om bollen går av fältet, placera den i mitten och väntar 3 sekunder.
   
   
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




