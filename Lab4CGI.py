#!/usr/bin/python37all
import cgi
import cgitb
import json
cgitb.enable()
data = cgi.FieldStorage()
LEDNum = data.getvalue('LED')
BrightnessNum = data.getvalue('Brightness')

dumpData = {'LED':LEDNum, 'Brightness':BrightnessNum}
with open('Lab4DataDump.txt','w') as f:
  json.dump(dumpData,f)

#Setting up html page
print('Content-type: text/html\n\n')
print('<html>')
print('<head>')
print('<title>Lab4</title>')# 
print('</head>')
print('<body>')
print('<div style="width:600px;background:#AAAAFF;border:1px;textalign:center">')
print('<br>')
print('<font size="3" color="black" face="helvetica">')

#adding in changing values
print('<form action="/cgi-bin/Lab4CGI.py" method="POST" target="_self">')
print('<input type="radio" name="LED" value="1"> LED 1 <br>')
print('<input type="radio" name="LED" value="2"> LED 2 <br>')
print('<input type="radio" name="LED" value="3"> LED 3 <br>')
print('<input type="range" name="brightness" min="0" max="100" value="',BrightnessNum,'"><br>')

print('<b>',cgi.FieldStorage.getlist(),'</b')


print ('<br>')
print ('</body>')
print ('</html>')