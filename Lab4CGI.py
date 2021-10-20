#!/usr/bin/python37all
import cgi
import cgitb
import json

cgitb.enable()
data = cgi.FieldStorage()

LED = data.getvalue('LEDpin')
Brightness = data.getvalue('BrightVal')
dataDump = {'LEDpin':LED,'BrightVal':Brightness}
with open('Lab4DataDump.txt', 'w') as f:
  json.dump(dataDump,f)

print('Content-type: text/html\n\n')
print('''
<html>
<form action="/cgi-bin/4cgi.py" method="POST">
  <input type="radio" name="LEDPin" value="1"> LED 1 <br>
  <input type="radio" name="LEDPin" value="2"> LED 2 <br>
  <input type="radio" name="LEDPin" value="3"> LED 3 <br>
  <input type="submit" value="Submit">
''')
print('<input type="range" name="BrightBal" min="0" max="100" value="%s"><br>' % Brightness)
print('</form>')
print('<b>Brightness = %s</b>' % Brightness)
print('</html>')