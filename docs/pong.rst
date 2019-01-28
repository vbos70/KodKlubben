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
med kommandot ``cd pgzero/pong``. Se :doc:`terminal` för mera kommandon.

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

Aktörerna har en position som har en X och en Y-koordinat, t.ex. (0,0)
och (50, 211). Aktörerna har också en *hastighet*. Hastigheten ändrar
en aktörs position *från ett ögonblick till ett annat*. I *Pong* har
hastigheten en *X-riktning* och en *Y-riktning*. X-riktningen ändrar
en aktörs X-koordinat och Y-riktningen ändrar en aktörs
Y-koordinat. När hastighetens X-riktning (eller Y-riktning) är 0,
ändrar aktörens X-koordinat (eller Y-koordinat) inte.

Till exempel, om bollen har positionen (50, 211) och X-hastigheten är
2 och Y-hastigheten är 3, så är bollens nästa position (52,
214). Dvs., bollen rör sig till höger (från X-koordinat 50 till 52)
och neråt (från Y-koordinat 211 till 214).

Det är också möjligt att bollen rör sig till vänster och uppåt. Om
bollen börjar igen på (50, 211) och dess nästa position är (49, 209),
vad är bollens X och Y-hastighet? För att komma från 50 till 49, tar
man 50 - 1. Alltså bollens X-hastighet är **-1**, ett *negativt* tal!
Och för att komma från 211 till 209 tar man 211 - 2. Vi ser att också
bollens Y-hastighet är negativ: **-2**. Det känns kanske lite konstigt
att hastigheten kann vara negativ, men för datorer är negativa tal
ingen problem. Vi valde att ha både positiva och negativa hastigheter
för det gör *Pongs* kod enklare.

Nu vet vi att bollen flytter sig med positiva eller negativa
hastigheter. Det ger bollen möjligheten att komma var som helst på
spelfältet.

Enligt *Pongs* reglarna går spelarna bara upp och ner. I *Pongs* kod
har vi därfor ingen X-hastighet för spelarna. Spelarnas Y-hastighet
kan, lika som bollens Y-hastighet, vara positiv och negativ. När en
spelare går uppåt är hans Y-hastighet negativ och hans Y-koordinat
blir mindre. När en spelare går neråt är hans Y-hastighet positiv och
hans Y-koordinat blir större.

Hur långt tar det *från ett ögonblick till ett annat*? Om
X-hastigheten är 2 och det tar bara en pytteliten del av en sekund
från ett ögonblick till et annat, så rör aktören sig snabbt över
*Pongs* spelfältet. Men om det tar en timme mellan två ögonblick, så
blir spelet ospelbar för det tar en evighet innan aktören har flyttat
sig. Det blir redan tråkigt med 1 sekund mellan två ögonblick.

Exakt hur långt det tar mellan två ögonblick i *Pong* vet vi inte. Det
beror på *pgzeros* kod och försöka att förstå den blir för mycket.
Genom att experimentera med olika hastigheter, hittar du nånting som
funkar bra. För *Pong* funkar det bra om hastigheter är maximalt 3
(postiv eller negativ), men du kan ändra det om du tycker det går för
långsamt.

Obs. I *Pongs* kod, heter hastighet ``SPEED`` (på engelska).

.. _main-loop:

Pongs 'main loop'
-----------------

*Pong* har ett visst antal steg som körs om och om och om tills spelet
är slut. Denna steg ar spelets 'main loop'. En 'main loop' beräknar
först hur aktörerna påverka varandra och vad deras nya positioner
är. Sedan uppdaterar 'main loop'-en skärmen enligt denna nya
positioner. Till slut börjar den på nytt med det första steget.

I *Pong* har 'main loop'-en den följande steg:
 
1. Ändrar spelarnas hastighet beroende på tangenterna som trycks in.

2. Ändrar spelarnas position beroende på deras hastighet.
   
3. Ändrar bollens position beroende på denns hastighet (båda i X och Y-riktning).

4. Om en spelare slår bollen, ändrar bollens hastighet.

5. Om bollen rör på toppen av fältet, ändrar dess Y-riktning neråt.

6. Om bollen rör på botten av fältet, ändrar dess Y-riktning uppåt.

7. Om bollen går av fältet, placera den i mitten och väntar 3 sekunder.

8. Uppdatera skärmen med aktörernas nya positioner.

I *Pongs* kod hittar vi steg 1--7 i funktionen ``update`` och steg 8 i
funktionen ``draw``. Kod för 'main loop'-en finns inte i *pong.py*
filen. Istället finns 'main loop's kod i *pgzeros* filer. För att
förstå hur *Pong* funkar behöver vi inte fördjupa oss i *pgzeros*
kod. Det räcker med att förstå steg 1--8 och deras relation med
funkionerna ``update`` och ``draw``.

Röra högra spelaren
-------------------

1. Öppna *pong.py* i din textredigerara ('text editor'), t.ex *Thonny
   IDE* eller *Idle*.

   Försök hitta `funktioner `draw`` och ``update``!

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
   genom att kolla linjerna for vänstra spelaren (``player1``) kan du
   skriva kodlinjer som får högra spelaren att röra sig upp med
   ``i``-knappen och ner med ``m`` knappen.

   Kodlinjerna som ska ändras har nu ordet ``pass``.




