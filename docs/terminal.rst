Terminal, shell, och kommandot
==============================


Terminal och shell
------------------

Terminalen är en fönster som kör en 'shell' och 'shell'-et läser in
kommandot du skriver och, om du har skrivit rätt, utför den. Det finns
många olika terminal-program och alla ser inte exakt likada
ut. Terminalen jag använder ser ut som här:

.. image:: images/terminal.png

Terminalen visar ``victor : bash`` under det stora textfälltet. Det
betyder att terminalens 'shell' heter 'bash' och användarens 'user
name' är victor.

Textfälltet är var 'shell'-et körs. Det är här man skrivar kommandot.

Shell
-----

'Shell'-et har en prompt och en markör som anger var du skrivar din
nästa kommandot. Vanligtvis är prompten symbolen ``$`` och markören en
fylld rektangel (på bilden övanpå är markören ihålig, men det beror på
att terminalens fönster var inaktiverat när bilden tog).

'Shell'-et vet vad din *nuvarande mapp* är och utför dina kommandot
altid i den nuvarande mapp. Det finns en mycket använt kommando för
att ändra nuvarande mappen tills en annan mapp: ``cd``, se nedan.


Kommandot
---------

Här är några kommandot du kann skriva i terminalen:

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


