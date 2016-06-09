# -*- coding: utf-8 -*-
import re
import urllib2

onlyid = []
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
		s += str([x for x in onlyid if onlyid.count(x)==1]).replace("[]", '').replace('/watch_videoshelf":', '').replace("['']", '').replace("&", "")[1:-1]

	count = 0
	v = ""
	for j in s:
		count += 1
		v += str(j).replace("'", "").replace("'", "")
		if count == 13:
			onetime.append(v)
			count = 0
			v = ""

	print onetime,'\n'

#getID()
#getID("https://www.youtube.com/playlist?list=PLq_0uf5RiXNoX6-DfIJ8R1su2eQp0aNg8", "")
#getID("https://www.youtube.com/playlist?list=PL0LVG0VoEMm1uh9PtE8JWjqq4-PfmQYhA", "")
#getID("https://www.youtube.com/playlist?list=PL0LVG0VoEMm2zg3wYvawpDiC3wcOvHqfb", "")
#getID("https://www.youtube.com/playlist?list=PL0LVG0VoEMm0P7fmJLdQCYl9XgsJl3kvT", "")