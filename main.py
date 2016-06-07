from flask import Flask
from template.youtube import HTML_TEMPLATE
import random

# get the ids from either using regex straights from the api 
# orr... just regexp from the youtube site.
ids = ('N7sid22OMV0', 'ZjE9V6b3sDI', 'ECwzgqRK7BQ')

app = Flask(__name__)
@app.route('/')
def homepage():
	vhtml = HTML_TEMPLATE.substitute(yt_id=ids[random.randint(0,50)])
	return """<h1>KlausWunderlich.se</h1>""" + vhtml

@app.route('/videos/<vid>')
def videos(vid):
	return HTML_TEMPLATE.substitute(yt_id=vid)
	
@app.route('/klaus')
def klaus():
	return "Hello World, Welcome to klaus Town... show Dj Telefon video"

if __name__ == '__main__':
	# remember to take of debug when rolling into production :3... if not i will get reeekt
	app.run(debug=True, use_reloader=True)
