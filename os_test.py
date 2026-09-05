import os
import urllib.request
import json
import xml.dom.minidom
doc = xml.dom.minidom.parse("note.xml")
print(doc.nodeName)
print(doc.firstChild.tagName)
skills = doc.getElementsByTagName("to")
web_url = urllib.request.urlopen('http://example.com')

#to print the status code and content of the webpage
print(web_url.getcode())
print(web_url.read())
# printing the Json data
theJsondata = json.loads(web_url.read())
print(theJsondata)  
#print(os.name)
#print(os.getcwd())
