#!/usr/bin/python37all

import cgi
import json
data = cgi.FieldStorage()
LEDNum = data.getvalue('LED')
BrightnessNum = data.getvalue('Brightness')

dumpData = {'LED':LEDNum, 'Brightness':BrightnessNum}
with open('Lab4DataDup.txt','w') as f:
  json.dump(dumpData,f)

print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/Lab4CGI.py" method="Post">')
print('selection = ' + LEDNum)
print('<input type="range" name="brightness" min="0" max="100" value="%s"><br>' % BrightnessNum)
print('</form>')
print('<Brightness is %s' %BrightnessNum)
print('</html>')