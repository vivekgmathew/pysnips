import urllib.request
from xml.etree.ElementTree import XML
import sys


# raise SystemExit("I am stopping here :)")

# Commandline Arguments
if len(sys.argv) != 3:
    raise SystemExit('Usage : file.py route stopid')

route = sys.argv[1]
stop_id = sys.argv[2]

# Url Request
bus_q = urllib.request.\
    urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop={}&route={}'.format(route, stop_id))
bus_data = bus_q.read()

# XML Parsing
xml_bus_data = XML(bus_data)
for pt in xml_bus_data.findall('.//pt'):
    print(pt.text)


# With context
with open('file.txt') as fh:
    for line in fh:
        line = line.strip()
        print(line)


