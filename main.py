import random
from flask import Flask
from template.youtube import HTML_TEMPLATE
from modules.getRandItem import getRandItem
from modules.getID import getID

# get the ids from either using regex straights from the api 
# orr... just regexp from the youtube site.
#ids = ('N7sid22OMV0', 'ZjE9V6b3sDI', 'ECwzgqRK7BQ')
ids = ['Dnqfnx6wlnE', 'MfhYMu0DYcU', 'tYa0bu6VrY0', '-n0LOL7-a2A', 'vXJxpFa1h64&', 'QwfQf4DrB8I', 'MQXumwBj_zw', 'Do3HGayT09E', 'SDQEc79h1Hw', 'SJhqa7J8fn4', 'sJzkjjvgIe8', 'DgxS--0o_vM', '0mMUljKRZ8s', 'j88FHHjkEhQ', 'I9OebCwkWQY', 's6aofFXnKJA', 'ZE6PqSD7_Fw', 'NcS1rEoLew8', 'zQKiZENUbxk', '99VkOnilq18', 'BZRlreOTFLI', '4EteTwLMGHU', 'B6u7VcGGdpU', 'DczXAgnnpOA', '9rwDJEk9GMw', 'gELGHZF5nqQ', 'bjDp12oNltA', 'C2_Rp-scits', 'uzHF5WUIm_Y', 'JUHQjTjtp4Y', 'Oxo2GxrzMDI', 'Vn0nZeXFffY', '2nrnBxSE6PE', 'A3Q3v8gkRKQ', 'y51Sb6buvjw', 'se-M1adlBX8', 'aBCX0FQMqGI', 'FCMUEQ6HJnk', '_uMEyTrlh_E', '8Wk7M3BWhnE', '987qrjGglrI', 'eHYi6UD2XNg', 'usaSlTD0CJc', 'tWlJOgpndFw', 'cGPnWfCziWI', 'u0AYa8yfyAM', 'gihRGkmA1Ns', 'MB31sSBMZ_I', 'UF4rlTLu_Kg', '05o2NQC4cx4', 'yPfPaJaVEVQ', 'ZZEAGQl3e6w', 's5eyIsmzR1s', 'YtWcYYLMboM', 'Wz_c4jclCD8', 'NCjgXQ6IGOU', 'IiPZFKTvncQ', 'drDLvcf85Rc', 'B38AFJbHmh0', 'PCOlB2nms_g', 'Ty_fZkEoInA', 'DjzOylqfukE', 'GueUDgJ4V1w', 'Wd1oKNsmeyQ', 'iPsllAmuV6M', '4Y2sRiITP9w', 'cRK3uyDoi0M', 'ZjE9V6b3sDI', 'BJy2pejQZTU', 'D7g3pSudTIM', 'aF8PP8OyrCk', 'oJuyXlydm_E', 'ivoQV2TtZTc', 'iQI2DOT6FQ4', 'W-ibNfEwIoY', 'AtE3f2jaBWE', '47HNRGdd2RU', 'v2pY6GVdgcQ', '&SUehSzRztY', 'ErjTXx0uTsQ', 'IuGg89BzWwq', 'UwgITcII2qo', '08N5Sand-c-', 'QFwnYxrrEER', 'IFqp9xOWPZB', 'A_lTDoqi4JN', 'MxXbgITxeu9', 'k35nMrK6q3F', 'MdIeTPjDznU', 'g4rkVPvFqav']
#ids = getID("https://www.youtube.com/playlist?list=PLq_0uf5RiXNoX6-DfIJ8R1su2eQp0aNg8", "")
rand = getRandItem(ids)

app = Flask(__name__)
@app.route('/')
def homepage():
	vhtml = HTML_TEMPLATE.substitute(yt_id=rand)
	return """<h1>KlausWunderlich.se</h1>""" + vhtml

@app.route('/videos/<vid>')
def videos(vid):
	return HTML_TEMPLATE.substitute(yt_id=vid)
	
if __name__ == '__main__':
	app.run(host="0.0.0.0",port=5000 ,debug=True, use_reloader=True)
