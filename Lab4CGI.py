#!/usr/bin/python37all
import cgi
import cgitb
import json

cgitb.enable()
data = cgi.FieldStorage()

LED = data.getvalue('LEDpin')
Brightness = data.getvalue('BrightVal')
dataDump = {'LED':LED,'BrightVal':Brightness}
with open('Lab4DataDump.txt', 'w') as f:
  json.dump(dataDump,f)

print('Content-type: text/html\n\n')
print('''
<html>
<form action="/cgi-bin/Lab4CGI.py" method="POST">
  <input type="radio" name="LED" value="1" checked> LED 1 <br>
  <input type="radio" name="LED" value="2"> LED 2 <br>
  <input type="radio" name="LED" value="3"> LED 3 <br>
  <input type="submit" value="Submit">
''')
print('<input type="range" name="BrightVal" min="0" max="100" value="%s"><br>' % Brightness)
print('</form>')
print('<b>Brightness = %s</b>' % Brightness)
print('</html>')