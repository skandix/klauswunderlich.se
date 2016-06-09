import random
from flask import Flask
from flask import render_template
from static.index import INDEX_TEMPLATE
from static.klaus import KLAUS_TEMPLATE
from modules.getRandItem import getRandItem
from modules.getYTstatus import getYTstatus
#from modules.getID import getID
from modules.getSCode import is_url_ok

# get the ids from either using regex straights from the api 
# orr... just regexp from the youtube site.
#ids = ('N7sid22OMV0', 'ZjE9V6b3sDI', 'ECwzgqRK7BQ')
ids = ['Dnqfnx6wlnE', 'MfhYMu0DYcU', 'tYa0bu6VrY0', '-n0LOL7-a2A', 'vXJxpFa1h64', 'QwfQf4Dr8I', 'MQXumwBj_zw', 'Do3HGaT09E', 'SDQEc79h1Hw', 'SJhqa7J8fn4', 'sJzkjjvgIe8', 'DgxS--0o_vM', '0mMUljKRZ8s', 'j88FHHjkEhQ', 'I9OebCwkWQY', 's6aofFXnKJA', 'ZE6PqSD7_Fw', 'NcS1rEoLew8', 'zQKiZENUbxk', '99VkOnilq18', 'BZRlreOTFLI', '4EteTwLMGHU', 'B6u7VcGGdpU', 'DczXAgnnpOA', '9rwDJEk9GMw', 'gELGHZF5nqQ', 'bjDp12oNltA', 'C2_Rp-scits', 'uzHF5WUIm_Y', 'JUHQjTjtp4Y', 'Oxo2GxrzMDI', 'Vn0nZeXFffY', '2nrnBxSE6PE', 'A3Q3v8gkRKQ', 'y51Sb6buvjw', 'se-M1adlBX8', 'aBCX0FQMqGI', 'FCMUEQ6HJnk', '_uMEyTrlh_E', '8Wk7M3BWhnE', '987qrjGglrI', 'eHYi6UD2XNg', 'usaSlTD0CJc', 'tWlJOgpndFw', 'cGPnWfCziWI', 'u0AYa8yfyAM', 'gihRGkmA1Ns', 'MB31sSBMZ_I', 'UF4rlTLu_Kg', '05o2NQC4cx4', 'yPfPaJaVEVQ', 'ZZEAGQl3e6w', 's5eyIsmzR1s', 'YtWcYYLMboM', 'Wz_c4jclCD8', 'NCjgXQ6IGOU', 'IiPZFKTvncQ', 'drDLvcf85Rc', 'B38AFJbHmh0', 'PCOlB2nms_g', 'Ty_fZkEoInA', 'DjzOylqfukE', 'GueUDgJ4V1w', 'Wd1oKNsmeyQ', 'iPsllAmuV6M', '4Y2sRiITP9w', 'cRK3uyDoi0M', 'ZjE9V6b3sDI', 'BJy2pejQZTU', 'D7g3pSudTIM', 'aF8PP8OyrCk', 'oJuyXlydm_E', 'ivoQV2TtZTc', 'iQI2DOT6FQ4', 'W-ibNfEwIoY', 'AtE3f2jaBWE', '47HNRGdd2RU', 'v2pY6GVdgcQ', 'SUehSzRztYE', 'rjTXx0uTsQI', 'uGg89BzWwqU', 'wgITcII2qo0', '8N5Sand-c-Q', 'FwnYxrrEERI', 'Fqp9xOWPZBA', '_lTDoqi4JNM', 'xXbgITxeu9k', '35nMrK6q3FM', 'dIeTPjDznUg', '4rkVPvFqavk','fS1YmFziG_8', 'N7sid22OMV0', 'Mm8CS8mNteM', 'ZjE9V6b3sDI', 'B38AFJbHmh0', '29RU-3q_p9U', 'ECwzgqRK7BQ', 'CsuXOcSnlgc', 'A3Q3v8gkRKQ', 'QwfQf4DrB8I', 'Pe_mYWOtSRQ', 'a6WXX4IeDPQ', 'C2rbvpctPho', 'sy3suFpKrnc', 'mvEdiDoGXXY', 'VFOecIMnLfw', '6iosekcqqNE', 'FCMUEQ6HJnk', 'ZPy9YPS6cRk', 'mw5ANDZzxu4', '_xPKPkfghnM', '_rZk8HrV3xs', 'CzJQI3fN1GU', 'jSndmsSxMmE', 'uCk_Z94BwD0', 'drhJBBfKGXQ', 'h2DS97HExcQ', 'lQJpyMKjWKQ', 'ZAMqq8jj02Q', 'Uf9qYsQKGxg', 'p4WdwkqhpdU', '8GnCYHMBFp4', 'XqPd9kAp3gc', '7rZPSxok1-c', 'JpKz-sPr_xw', 'IUpIn0Jo5IU', 'uzHF5WUIm_Y', 'UcjpRrDzieM', 'Uo14NsDRO3E', 'BwmYINtRagU', 'UNPy9axowLs', 'BvzlblafwIk', 'iJZ29wiVwmQ', 'zD1zqeZ5JzU', 'UinCp3DxItA', 'rzajKJp1bdw', 'I9OebCwkWQY', 'ZAzGDsGosiw', 'Y1xViIvXaB8', 'aFJo6NaO3CU', 'Ul6W0X2G-cI', 'Qb-P_AcCjWY', 'MB31sSBMZ_I', '0evz8aFOMiM', 'h8nmDbLL4kk', 'ClseSMWRJhc', '0L4hoKgiW-U', 'XyNR2cUNSsU', 'iEcQYkCsd0E', 'gwWxDJQVIQc', 'WUnuGFIjQgI', 'Fap7ICP-g9w', 'mDS7Nyh_Zo4', 'pPAXd4iTVms', 'IBD0Y7-A_sQ', 'VxWU1cCserE', 'GQ3NMniypb0', 'SWbCz0yQYbA', '8Dt7D6XjW7A', 'sBhoMNA9Om8', 'LSRDEoQ5wpk', 'rFSugQ3NVmo', 'UF4rlTLu_Kg', 'vNpmftXUGaA', '8C-rFrztaPg', 'oeC198mtfg8', 'H_I536feV3s', 'jznTb0vzpAo', 'fYLh1yHbFjo', 'PZAEffczZik', 'yBLPn_FlAfs', 'PUXqGymkOc4', '31GLPccIFmQ', 'MgdlMddTjbM', 'lVFxHTatfz4', 'VYkRIn9Bi-s', 'wE6OG8wisT8', 'NDZzcxMFDFc', '5njQcUkucX8', 'RDYeDbi_SHo', 'j1y92gDSH20', '8RojHLAVzwQ', 'rzgcu7oTt44', 'LUN_GusMxuA', 'AmB0DcdvqlA', 'XD_GIykO3vw', 'oVUtlOuveTE', 'DfLHmIBNev0', 'YX_C-b-L13s', 'WsNX4-ha_xU', 'gAZYCMIkgTw', '30mLXRTmxAc', '5wHs6MFRJd0', 'l9l7q5ORBoA', '_Y6LmvCR1LQ', 'sQbIfKAqMYY', 'U5omgYaT0cM', 'r81jJm7hJ78', 'emZQP-s5F_Y', 'ACShAPbgxKM', 'hVcI354O7wY', 'T8pnBrsTSRA', 'kkOPNKX8OZc', 'MpPuzYQBzXo', 'ZC1eifqAAqg', 'rMQ3Me5ushI', 'GETKiGJJDzs', 'Oqvxt3htZ9k', 'Eb5iDHKMxws', 'vYzzrG8S4PM', 'NBI1QZvnFqk', '6sDor9-_ENw', '1hWdE3Ccz98', 'CcKyvBKwrx8', 'DdfSitGhH-A', 'dKA7fTWXVJY', 'AQ55xqfDW7c', 'dWPUDUawdV0', 'opkLtZEsmjE', 'AfjPY02baw4','aagSAAqZZaw', 'hQV_f7Iw45A', 'TNEjqPZFyYg', 'yTGUEt7Eiu0', '10ntQmUtWvQ', 'tjs96ny6oYw', 'rlzXgBnLIJ8', '6lx5lXFdTHY', 'OjU1BQXAEV8', 'qFqw7bY5TQ8', 'm4Zu0K0xk-o','lShug56Y-rc', 'uYxJqi50sso', 'VBclA6lQ9Qg', '8oTn3y0dPsk', '2jh3xl0S3OE', 'p7o_9-Cs220', 'UR2LcB9wGs0', 'LFDxNggZ0PY', 'B9h0meKQi8E', '9EpE0suQmXg', 'WMcDfrXfmOM', 'HJWjuJDQaeE', 'LGeFi5E9NX8', 'Oeq7Oj5apPI', 'hopYXDBQIso', 'QjdxzBW3-ZE', 'sTLdVHbd_mo', 'm9qrOlB7-aw', '-G2L7I5QCrE', 'PAdxi6tUNlg', '_NBOw_pRmT0', 'A-uFrHQXShY', 'YeBGwCkHct0', 'NDhvSfFlzlo', '4LxcH_LZdIw', '1JRPI3JiTBI', 'WOgu_tMkNLw', 'Bzo7A0zxCFQ', 'h3IA0iPG2Fg', 'kWrVjw0WfQM', 'x5GHiLkyMT0', 'GBO0ps38X88', '3du5x8wipKU', '6jfB_fchGsk', 'FnjJ93T12F0', 'UkNBHTIBxKM', '9nzdIN5NWU0', 'jLFfq55gvIs', 'TnKhSaQ-9XQ', 'JPA_tn4rYCY', '8SROxB18YA8', 'bx7LZzcTkTQ', 'SmX2w2TBv0w', 'E7XybMkAhzs', 'gFnufv6BFLU', 'xxtzLAodA28']
#ids = getID("https://www.youtube.com/playlist?list=PLq_0uf5RiXNoX6-DfIJ8R1su2eQp0aNg8", "")

app = Flask(__name__)
@app.route('/',)
def homepage():
	rand = getRandItem(ids)
	yt_url = 'https://www.youtube.com/watch?v={video_id}'.format(video_id=rand)
	vhtml = INDEX_TEMPLATE.substitute(yt_id=rand)

	if getYTstatus(yt_url) == False:
		return """<h1>klauswunderlich.se</h1>""" + vhtml

	else:
		return """<h1> Things are going bit too fast, Please standby</h1>
		<img src="https://scontent-frt3-1.cdninstagram.com/t51.2885-15/e35/12479068_275523542785751_1955961211_n.jpg?ig_cache_key=MTIzNTI5OTc5Mzg5NTExMzkxNQ%3D%3D.2">
		<script> location.reload();</script>""", 404


@app.route('/videos/<vid>')
def videos(vid):
	yt_url = 'https://www.youtube.com/watch?v={video_id}'.format(video_id=vid)
	
	if True == is_url_ok(yt_url):
		return "Youtube video {video_id} exists".format(video_id=vid)

	else:
    		html = "YouTube video {video_id} DOES NOT exist".format(video_id=vid)
        return html, 404

@app.route('/klaus')
def klaus():
	khtml = KLAUS_TEMPLATE.substitute()
	return khtml


if __name__ == '__main__':
	app.run(host="0.0.0.0",port=80 ,debug=False, use_reloader=True)
