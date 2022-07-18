# Using Web Services
# https://www.py4e.com/lessons/servces
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET


url = input("Enter Location: ")


print("Retrieving URL: ", url)


xml = urllib.request.urlopen(url).read()



chars = len(xml)


print("Retrieved: ", chars, "characters")



sums = 0
temp = 0


tree = ET.fromstring(xml)


counts = tree.findall('.//count')