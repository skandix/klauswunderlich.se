import requests
import urllib2
import re

def is_url_ok(url):
	return 200 == requests.head(url).status_code

def getYTstatus(url):
	rwHtml = urllib2.urlopen(url).read()
	regexp = re.compile(ur'"submessage">\s+\w+')
	loot = re.findall(regexp, rwHtml)
	if loot:
		return True
	else:
		return False