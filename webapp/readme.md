# Web App #

To run the *app.py* web app, do this:

    $ python3 app.py

     * Serving Flask app "app" (lazy loading)
     * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: on
     * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 599-252-347

Now the web server is running the *app.py* application. You can check 
this in your web browser by going to http://127.0.0.1:5000/

# Using the IP address #

If you know the IP address of your computer, you can try to reach your 
web application via the IP address. This does not work for a global IP 
address, but on a computer (or phone) on the same local net, it might 
work.

Suppose your IP address is 192.168.100.11, then on the other computer 
(or phone), you should use the url: http://192.168.100.11:5000/

Note: the local address might be different than what you see here. 


# Find out what your IP addresses are #

If you are on WiFi use the command: 

    $ ifconfig wlan0

If you are on an ethernet (i.e., ethernet cable), use the command:

    $ ifconfig eth0

If you don't know what kind of network you are connected too, use:

    $ ifconfig

The output looks like this:

    eth0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
            ether b8:27:eb:29:25:fe  txqueuelen 1000  (Ethernet)
            RX packets 0  bytes 0 (0.0 B)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 0  bytes 0 (0.0 B)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
    
    lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
            inet 127.0.0.1  netmask 255.0.0.0
            inet6 ::1  prefixlen 128  scopeid 0x10<host>
            loop  txqueuelen 1000  (Local Loopback)
            RX packets 70  bytes 6147 (6.0 KiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 70  bytes 6147 (6.0 KiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
    
    wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 192.168.100.11  netmask 255.255.255.0  broadcast 192.168.100.255
            inet6 fe80::225a:4f23:fe7c:1e1b  prefixlen 64  scopeid 0x20<link>
            ether b8:27:eb:7c:70:ab  txqueuelen 1000  (Ethernet)
            RX packets 11598  bytes 12830604 (12.2 MiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 7821  bytes 924611 (902.9 KiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

In each section, look for a line starting with *inet*.

Above, the *eth0:* section does not contain an *inet* line. Therefore, 
this computer is not connected to an Ethernet network.

The *lo:* section contains an *inet* line with the IP address 127.0.0.1. 
This is a special IP address via which you can reach only the local 
machine itself.

The *wlan0:* section contains an *inet* line with the IP address 
192.168.100.11. This is the IP address on the WiFi network to which the 
computer is connected.
