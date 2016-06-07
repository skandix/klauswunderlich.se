import random
from flask import Flask
from template.youtube import HTML_TEMPLATE
from modules.getRandItem import getRandItem
from modules.getID import getID

# get the ids from either using regex straights from the api 
# orr... just regexp from the youtube site.
#ids = ('N7sid22OMV0', 'ZjE9V6b3sDI', 'ECwzgqRK7BQ')
ids = getID("https://www.youtube.com/playlist?list=PLq_0uf5RiXNoX6-DfIJ8R1su2eQp0aNg8", "")

rand = getRandItem(ids)

app = Flask(__name__)
@app.route('/')
def homepage():
	vhtml = HTML_TEMPLATE.substitute(yt_id=rand)
	return """<h1>KlausWunderlich.se</h1>""" + vhtml
	print rand

@app.route('/videos/<vid>')
def videos(vid):
	return HTML_TEMPLATE.substitute(yt_id=vid)
	
if __name__ == '__main__':
	app.run(host="0.0.0.0",port=80 ,debug=True, use_reloader=True)
