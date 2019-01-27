Terminal, shell, och kommando
=============================


Terminal
--------

Terminalen är en fönster som kör en 'shell' och 'shell'-et läser in
kommandon du skriver och (om du har skrivit rätt) utför den. Det finns
många olika terminalen och dom kan ser olika ut. Terminalen jag
använder heter *Konsole* och ser ut som här:

.. image:: images/terminal.png

Den här terminalen visar ``victor : bash`` under det stora
textfälltet. Det betyder att terminalens 'shell' heter 'bash' och
användarens 'user name' är victor.

Du ger/skrivar kommandon i textfälltet och 'shell'-et ger kommandons
resultat och andra meddelanden också i textfälltet. 

Shell
-----

'Shell'-et har en prompt och en markör som anger var du skrivar dit
nästa kommandot. Vanligtvis är prompten symbolen ``$`` och markören en
fylld rektangel (på bilden övanpå är markören ihålig, men det beror på
att terminalens fönster var inaktiverat när bilden togs).

'Shell'-et vet vad din *nuvarande mapp* är och utför dina kommando
alltid i den nuvarande mapp. Det finns ett mycket använt kommando för
att ändra nuvarande mappen tills en annan mapp: ``cd``, se nedan.


Kommandon
---------

Här är några kommandon du kann skriva i terminalen:

``cd``

  'change directory': byta mapp. Ändrar 'shell'-ets nuvarande mapp
  till angiven mapp. Utan angiven mapp händer ingenting. ``..`` kan
  användas för mappen som innehåller nuvarande mappen.

``ls``

  'list files': visa filer. Visar namn på filerna som finns i angiven mapp.

``pwd``

  'print working directory': visa nuvarande mapp. Visar namnet
  på 'shell'-et nuvarande mapp.

``poweroff``

  Stänger av datorn.

``reboot``

  Startar om datorn
  
``python3``

  Kör den 'Python3 interpreter' som kann utföra Python 3
  program.

  Obs., det finns också en 'Python 2 interpreter' som man kör med
  kommandot ``python`` (utan 2!). 'Python 3' och 'Python 2' är
  olika. I Kodklubben använder vi mest Python 3.

``pgzrun``

  Kör angiven 'pgzero' spel. Vi användar 'pgzero' för att skriva och
  köra vår egna spel. Mera om 'pgzero' hittar du här på `pgzero`_'s
  websida.


.. _pgzero: https://pygame-zero.readthedocs.io/en/stable/


