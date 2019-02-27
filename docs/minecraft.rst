Minecraft
=========

Jag beskriver kort hur man programmerar Minecraft i Python. Mera
information finns på olika websidor, se `Minecraft länkar`_.

Köra din kod
------------

För att köra kod, spara du det i en Python fil (som kallas
t.ex. `minkod.py`) och sedan ger du följande kommandot i en terminal::

  python3 minkod.py
  
Obs. det funkar bara om du har startat ett Minecraft spel redan!


Pythons `mcpi` moduler
----------------------

Din kod ska importera `mcpi` moduler som ger åtkomst till Minecraft::

  from mcpi.minecraft import Minecraft
  from mcpi import block


Ansluta din kod till Minecraft
------------------------------

Den nästa rad ansluter variabelen `mc` till Minecraft::

  mc = Minecraft.create()

I resten of programmet använder du `mc` för att göra saker i Minecraft
spelet. Det är OK att välja en annan namn for variabelen `mc`. 

Obs. Om du glömde att starta Minecraft innan den här rad utförs,
krasha programmet! Dvs., du ska först starta Minecraft spelet och sen
köra din kod.

Posta till Minecraft chatten:
-----------------------------

Din kod kan chatta i Minecraft::
  
  mc.postToChat("Hej, jag kodar Minecraft i Python!")

Medelandet skrivs mellan `"` eller `'` symboler!

Skriva funktioner
-----------------

När du vill göra flera saker många gånger, är det bäst att skriva en
funktion. Sedan kan du använda funktionen när och var
du vill. Funktionen `jump_y` får spelaren (`mc.player`) att hoppa upp i
lyften (dvs., flytta i Y-riktningen) med en angiven höjd::

  def jump_y(distance_y):
      pos=mc.player.getPos()
      mc.player.setPos(pos.x, pos.y + distance_y, pos.z)
      
  jump_y(10)

Parametern `distance_y` är höjden (i meter). Den sista rad visar hur
man anropar funktionen `jump_y` för att får spelaren hoppa 10 meter
upp i lyften.

Kan du skriva en funktioner som flyttar spelaren i X-riktning och
Z-riktning? Här är en början::

  def jump_x(distance_x):
      pos=mc.player.getPos()
      mc.player.setPos(pos.x + ... , pos.y, pos.z)

  def jump_z(distance_z):
      pos=mc.player.getPos()
      mc.player.setPos(pos.x, pos.y, pos.z + ...)

Du ska ändra `...` för rätt kod i båda funktioner.
	
Här är en funktion som flyttar spelaren i alla tre riktningar på en
gång::

  def jump_xyz(distance_x, distance_y, distance_z):
      pos=mc.player.getPos()
      mc.player.setPos(pos.x + distance_x,
	                 pos.y + distance_y,
			 pos.z + distance_z)

  jump_xyz(4, 2, 10)

I den sista rad flyttas spelaren 4 meter i X-riktningen, 2 meter I
Y-riktningen, och 10 meter i Z-riktningen.

Vad händer om du ger negativa tal for några of parametern? T.ex.::

  jump_xyz(-4, 2, -10)

Bygga block
-----------

Bygga block gör man med funktionen `setBlock`. Här byggs en `STONE`
block på position (0, 0, 0)::

  mc.setBlock(0, 0, 0, block.STONE.id)

Obs. glöm inte `.id` efter `STONE`! Utan `.id` kan det funka, men
block med data funkar inte.

På sidan `Minecraft API`_ hittar du alla block sorter som finns i
Minecraft.
  
Om du kör den här kod, ska du flytta din spelara nära position (0,
0, 0) om du vill se resultatet. Istället för at bygga på (0, 0, 0), kan
du bygga nära spelarens nuvarande position::

  pos = mc.player.getPos()
  mc.setBlock(pos.x+2, pos.y, pos.z+2, block.STONE.id)

Här byggs en `STONE` block på lite mer än 2 meter från spelaren.

Om man vill bygga flera block på en gång, används funktionen
`setBlocks`. `setBlocks` fyller hela volumen mellan två angiven
punkter med samma block.  Här fylls volumen mellan `(pos.x+2, pos.y,
pos.z+2)` och `(pos.x+4,pos.y+5,pos.z+6)` med `STONE` block::
  
  pos = mc.player.getPos()
  mc.setBlocks(pos.x+2, pos.y, pos.z+2,
               pos.x+4, pos.y+5, pos.z+6,
	       block.STONE.id)

Obs. spelaren blir inbyggd om han befinner sig i volumen mellan
denna två punkter.

Block med data
~~~~~~~~~~~~~~

Några block finns i olika typer. Till exempel, `WOOL` finns i olika
färger som vit, magenta, grön, ... Block som finns i olika typer byggs
också med `setBlock` och `setBlocks`, men man kan la till en `data`
parameter som anger typen av block. Här byggs en volum av ull (`WOOL`)
i färgen magenta (2)::

  pos = mc.player.getPos()
  mc.setBlocks(pos.x+2, pos.y, pos.z+2,
               pos.x+4, pos.y+5, pos.z+6,
	       block.WOOL.id, 2)

TNT är också en block som har `data`. TNT's `data` kan var 0 (inaktiv)
eller 1 (aktiv). Aktiv TNT sprängs när spelaren slår på det::

  pos = mc.player.getPos()
  mc.setBlocks(pos.x+2, pos.y, pos.z+2,
               pos.x+4, pos.y+5, pos.z+6,
	       block.TNT.id, 1)
  
Se `Minecraft API`_ for alla olika `data` som finns.

Pyramid
-------

Här är en program som bygger an pyramid i Minecraft::

  from mcpi.minecraft import Minecraft
  from mcpi import block
  
  mc = Minecraft.create()
  
  x,y,z = mc.player.getTilePos()
  
  PYRAMID_SIZE = 5
  PYRAMID_BLOCK1 = block.STONE
  PYRAMID_BLOCK2 = block.GLOWSTONE_BLOCK
  OFFSET = 5
  
  # Create empy space to build the pyramid
  mc.setBlocks(x-PYRAMID_SIZE-2, y, z+OFFSET,
               x+PYRAMID_SIZE+2, y+PYRAMID_SIZE+2, + z+2*PYRAMID_SIZE+2,
               block.AIR.id)
  
  
  d = 0
  s = PYRAMID_BLOCK1
  
  for layer in range(PYRAMID_SIZE):
      mc.setBlocks(x-PYRAMID_SIZE+d, y+layer, z+OFFSET+d,
                   x+PYRAMID_SIZE-d, y+layer, z+OFFSET+(2*PYRAMID_SIZE - d),
                   s.id)
      d += 1
      if s == PYRAMID_BLOCK1:
          s = PYRAMID_BLOCK2
      else:
          s = PYRAMID_BLOCK1
  
  mc.player.setPos(x, PYRAMID_SIZE+10, PYRAMID_SIZE+OFFSET)
  



.. _Minecraft länkar:

Minecraft länkar
----------------

.. _Minecraft control keys: https://arghbox.files.wordpress.com/2013/07/minecraft-pi-controls.png

.. _Minecraft Python Challenges: https://www.101computing.net/minecraft-python-challenges

.. _Minecraft API: https://www.stuffaboutcode.com/p/minecraft-api-reference.html

.. _MagPi Minecraft Maker Guide: https://www.raspberrypi.org/magpi-issues/MagPi58.pdf

.. _mcpipy: https://github.com/brooksc/mcpipy


* `Minecraft control keys`_: Tangenter och musknapp man använder i
  Minecraft.
  
* `Minecraft Python Challenges`_: Enkla exempel som visar hur du
  programmerar Minecraft.

* `Minecraft API`_ : Mycket om Minecraft Python API.

* `MagPi Minecraft Maker Guide`_: Tidning om Raspberry Pi och Minecraft.

* `mcpipy`_: GitHub sidan med Python code för att programmera Minecraft.

