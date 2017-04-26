import xml.dom.minidom 
import string
import urllib2

## Looks up city in dictionnary for URL,
## @return xml data
def data_retriever(url_path):
	
	# Lookup in dictionnary for URL associated to city name
	request = urllib2.Request(url_path)
	
	# Fetch xml file from Environment Canada site
	response = urllib2.urlopen(request)
	
	xml_blob = xml.dom.minidom.parseString(response.read())
	
	return xml_blob

## Fetches appropriate info from Environment Canada RSS Feed and formats output
## @return [condition] temperature
def get_temperature(url_path):
	
	xml_blob = data_retriever(url_path)
	node_list = xml_blob.getElementsByTagName("title")
	
	for node in node_list:
		
		# Go through list until we reach desired line of xml_blob
		if "Current Conditions:" in node.firstChild.nodeValue:
			
			# Find the current weather conditions and/or temperature
			weather = string.split(node.firstChild.nodeValue, ": ", -1)
			
			# Free up that memory!
			xml_blob.unlink()
			
			return weather[1]
