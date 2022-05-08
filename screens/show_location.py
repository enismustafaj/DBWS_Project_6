#!/usr/bin/python3
import cgitb
import cgi
import mysql.connector
import requests
import json
import os
cgitb.enable()

print("Content-Type: text/html;charset=utf-8\n\n")
ip = cgi.escape(os.environ["REMOTE_ADDR"])
data = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=92c6928ce03d4d88be7fb86088d7ae10").json()
ip = data['ip_address']
a = float(data['longitude'])
b = float(data['latitude'])


html = '''
<html>
    <head>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css"
   integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A=="
   crossorigin=""/>
   <link rel = "stylesheet" href = ../../main.css">
   <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"
   integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA=="
   crossorigin=""></script>
    </head>

    <body>
    <h1 style="text-align:center">Your Location</a>
        <div id="mapid" style="height:50%; width:50%; margin:auto;margin-top:10%"></div>
        
        <script>
            var mymap = L.map('mapid').setView([{}, {}], 13);'''.format(b,a)
print(html)
body = str('''
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoiZW11c3RhZmFqIiwiYSI6ImNraTAyMjRoMTBnZHgyenFrc2V3ZDdtd3IifQ.kiXHYtmpSPptZIwGa16MqA'
}).addTo(mymap);

''')

last = '''
var marker = L.marker([{}, {}]).addTo(mymap);
marker.bindPopup("My IP address is {}");
        </script>
    </body>
</html>
'''.format(b,a,ip)

print(body)
print(last)