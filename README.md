# KodKlubben

Kod för Ingås kodare

## Vi börjar

Första gången ska vi

1. Bekanta oss med Raspberry Pi:
   1. Öppna "boxen"
   1. Ansluta allt
   1. Starta upp
   1. Stänga av
   1. Sätt in SD kortet
   1. Starta upp igen

   Se även
   https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started

1. Upptäcka vad Raspberry Pi kan

   Starta upp program som är redan installerat

1. Konfigurera wifi och Internetanslutning

   * wifi password

   * starta och testa webbrowsern 'chromium'

1. Spela 

1. Koda

   1. I chromiums startsida (search engine), sök: vbos70 KodKlubben

   1. Ladda ner '.zip' fil

      Klicka "Clone or download" och välja "Download zip"

   1. Extrahera filen

   1. Öppna Python kod i Thonny Python IDE

   1. Köra Python kod


## Andra gången: Python och Thonny

### Starta Thonny IDE

Leta fram och klicka Thonny IDE på meny.

![Raspbian meny](images/rpimenu.jpg)

När Thonny har startas up, ser du en fönster som den här:

![Thonny IDE](images/thonny.jpg)

#### Edit fönstret i Thonny

Edit fönstret är just under knapparna. Här skrivar man Python kod /
program som du kan spara i filer. Filnamnet visas övanpå fönstret. 
Här på bilden heter denn `<untitled>` (namnlös).

#### "Shell" fönstret i Thonny
 
Längst ner finns "Shell" fönstret som visar "Python":

```
Python 3.5.3 (/usr/bin/python3)
```

Här skriver man enskilda Python meningar som Python beräknar efter
du klicka `Enter`. Till exempel:

```
>>> 1+3
4

```

Här finns flera Python "expressions" (meningar) som du kan försoka:

  - `10 + 2 * 3`
  - `(10 + 2) * 3`
  - `1.5 - 0.32`
  
Python kan också räkna med "strings" (listor av bokstävar):

  - `"Hej, vad heter du"`
  - `'Hej, vad heter du' + "?"` 
  - `"Här kodar Ingås kodklubb!"`
  - `"Hej!" * 10` 

Strings börjar och slutar med `"` eller `'`.
  
##  26-09-2018: Turtle Graphics

Den här gången fortsätta vi med Python kod, men nu ska vi rita.

### Inan vi börjar

1. Tömma `Downloads` mappen

1. Ladda ner .zip filen från https://github.com/vbos70/KodKlubben

1. Extrahera .zip filen i `Downloads` mappen


### Starta Thonny IDE

1. Öppna filen

   `Downloads/KodKlubben-master/turtle/drawing1.py`

1. Kör (klicka gröna pil knappen)

![Turtle](images/turtle.jpg)


### Kan du ändra koden så att ...

1. den ritar flera cirklar?

1. den ritar röda cirklar?


### Mera turtle "commands"

Här ar flera turtle "commands". Testa vad dom gör i din kod.

- `forward(10)`
- `backward(10)`
- `left(90)`
- `right(90)`
- `stamp()`
- `speed(1)`
- `speed(10)`

Och det finns ännu flera commands på
[Python Turtle Graphics](https://docs.python.org/3/library/turtle.html)


# Programmera Minecraft


1. Starta Minecraft och skapa en new värld.

1. Lämna Minecraft fönstret i bakgrunden (`TAB`) och öppna Thonny Python IDE.

1. Koda i Python, se exempel.

1. Kör din kod och kolla vad händer i Minecraft fönstret.


## Här ar några exempel:

Kopiera den här exempel i Thonny Python IDE, spara filen (varje
exempel i en ny fil), och kör din kod.


### Posta till Minecraft chatten:


```
from mcpi import minecraft, block
 
mc = minecraft.Minecraft.create()
msg = "Hej! Jag kodar Minecraft."
mc.postToChat(msg)
```

###  Hoppa i lyften

```
from mcpi import minecraft, block
import time
 
def jump(distance):
    #Let's wait 1 second
    time.sleep(1)
    
    #Retrieve the X,Y,Z coordinates of the player
    pos=mc.player.getPos()
    #Change the Y coordinate of the player to position it up in the sky    
    mc.player.setPos(pos.x, pos.y + distance, pos.z)

# Connect to Minecraft 
mc = minecraft.Minecraft.create()

 
#Main Program Starts Here:
jump(100)
```

### Bygga med block

```
from mcpi import minecraft, block
import time
 
def createTower():
    #Let's wait 1 second
    time.sleep(1)
    
    #Retrieve the X,Y,Z coordinates of the player
    pos=mc.player.getPos()
 
    #Create a 10-block high tower, 5 blocks away from the player
    mc.setBlock(pos.x + 5, pos.y, pos.z, block.STONE)
    mc.setBlock(pos.x + 5, pos.y+1, pos.z, block.STONE)
    mc.setBlock(pos.x + 5, pos.y+2, pos.z, block.STONE)
    mc.setBlock(pos.x + 5, pos.y+3, pos.z, block.STONE)
    mc.setBlock(pos.x + 5, pos.y+4, pos.z, block.STONE)
    mc.setBlock(pos.x + 5, pos.y+5, pos.z, block.STONE)
    mc.setBlock(pos.x + 5, pos.y+6, pos.z, block.STONE)
    mc.setBlock(pos.x + 5, pos.y+7, pos.z, block.STONE)
    mc.setBlock(pos.x + 5, pos.y+8, pos.z, block.STONE)
    mc.setBlock(pos.x + 5, pos.y+9, pos.z, block.STONE)
    mc.setBlock(pos.x + 5, pos.y+10, pos.z, block.STONE)
 
# Connect to Minecraft 
mc = minecraft.Minecraft.create()

#Main Program Starts Here:
createTower()
```

### Bygga en Pyramid

```
from mcpi.minecraft import Minecraft
from mcpi import block

# Connect to Minecraft
mc = Minecraft.create()

# Determine the Player's current position.
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

mc.player.setPos(x, PYRAMID_SIZE+1, PYRAMID_SIZE+OFFSET)

```

## Links till Minecraft sidor



[[Minecraft control keys]](https://arghbox.files.wordpress.com/2013/07/minecraft-pi-controls.png): Hur du använder tangentbordet och mus i Minecraft.

[[Minecraft Python Challenges]](https://www.101computing.net/minecraft-python-challenges/): Enkla exempel som visar hur du programmerar Minecraft.


[[Minecraft API]](https://www.stuffaboutcode.com/p/minecraft-api-reference.html): Mycket om Minecraft Python API.


[[MagPi Minecraft Maker Guide]](https://www.raspberrypi.org/magpi-issues/MagPi58.pdf): Tidning om Raspberry Pi och Minecraft.

[[mcpipy]](https://github.com/brooksc/mcpipy): GitHub sidan med Python code för att programmera Minecraft.



# Labyrint

1. Ladda ner .zip filen, extrahera den, och öppa programmet `maze.py` i Thonny IDE.

1. Kör programmet några gånger


1. Fixa "function" `draw_trail` och kör programmet igen.

1. Om du fixade programmet rätt, så visas den en rut genom labyrinten.

![Maze](images/maze-example.jpg)
