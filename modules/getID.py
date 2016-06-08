# -*- coding: utf-8 -*-
import re
import urllib2

#all the added here
onlyid = []
# then filter out so each id only occurs once.
onetime = []
def getHTML(url):
	return urllib2.urlopen(url).read()

def getID(url, s):
	testStr = "'rjTXx0uTsQI'"

	rawHTML = getHTML(url)
	black_magic = re.compile(ur'\/watch.[v=]+[^+]{11}')
	loot = re.findall(black_magic, rawHTML)
	for i in loot:
		clean = i.replace('/watch?v=', '')
		onlyid.append(clean)
		#print onlyid[1:-1]
		s += str([x for x in onlyid if onlyid.count(x)==1]).replace("[]", '').replace('/watch_videoshelf":', '').replace("['']", '')[1:-1]

		#print s
	count = 0
	v = ""
	for j in s:
		count += 1
		v += str(j).replace("'", "")
		if count == 13:
			onetime.append(v)
			count = 0
			v = ""

	print onetime

#getID()
getID("https://www.youtube.com/playlist?list=PLq_0uf5RiXNoX6-DfIJ8R1su2eQp0aNg8", "")