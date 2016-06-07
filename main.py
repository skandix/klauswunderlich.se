from flask import Flask
from template.youtube import HTML_TEMPLATE

#ids = ('N7sid22OMV0', 'ZjE9V6b3sDI', 'ECwzgqRK7BQ')
#for j in ids:
#	print j

app = Flask(__name__)
@app.route('/')
def homepage():
	vhtml = HTML_TEMPLATE.substitute(yt_id=j)
	return """<h1>KlausWunderlich.se</h1>""" + vhtml

@app.route('/videos/<vid>')
def videos(vid):
	return HTML_TEMPLATE.substitute(yt_id=vid)

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)

