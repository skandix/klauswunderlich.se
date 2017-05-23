from flask import Flask, request, render_template
from modules.getRandItem import *
from modules.getYTstatus import *
from modules.getID import *
import logging
import random
import os


ids = getID("https://www.youtube.com/playlist?list=PL0LVG0VoEMm1uh9PtE8JWjqq4-PfmQYhA")


print ids
#logging.basicConfig(filename='logs/klaus.log',level=logging.DEBUG,format='%(message)s %(asctime)s')
#logging.info('-=Started Logging=- \n')


app = Flask(__name__)

@app.route('/',)
def homepage():

	rand = getRandItem(ids)
	yt_url = 'https://www.youtube.com/watch?v={video_id}'.format(video_id=rand)

	if getYTstatus(yt_url) == False:
		return render_template('index.html', yt_id=rand), 200

	else:
		return render_template('VideoNotFound.html'), 404

@app.route('/videos/<vid>')
def videos(vid):
	yt_url = 'https://www.youtube.com/watch?v={video_id}'.format(video_id=vid)
	
	if is_url_ok(yt_url) and getYTstatus(yt_url):
		return "Youtube video {video_id} exists".format(video_id=vid)

	else:
    		html = "YouTube video {video_id} DOES NOT exist".format(video_id=vid)
        return html, 404

@app.route('/klaus')
def klaus():
	return render_template('klaus.html'), 420

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 4020))
app.run(host="0.0.0.0",port=port)

# for use when running locally.. and debugging purposes
#app.run(host="0.0.0.0",port=8080 ,debug=True, use_reloader=True)