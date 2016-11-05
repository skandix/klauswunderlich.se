import urllib2
import re

def getYTstatus(url):
	rwHtml = urllib2.urlopen(url).read()
	regexp = re.compile(ur'"submessage">\s+\w+')
	loot = re.findall(regexp, rwHtml)
	if loot:
		return True
	else:
		return False


# uncomment to see that it works when something aren't avaliable, and when they are
# video not avaliable!
#print getYTstatus("https://www.youtube.com/watch?v=hopYXDBQIso")

# video avaliable
#print getYTstatus("https://www.youtube.com/watch?v=NCjgXQ6IGOU")