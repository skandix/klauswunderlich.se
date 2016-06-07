# -*- coding: utf-8 -*-
import requests

def get_latest_json(endpoint):                                                           
    return requests.get(endpoint, stream=True, headers=headers).json()

def get_id(s):
	yt_id = get_latest_json("https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=PL0LVG0VoEMm1EIsMin90Am-ddlpMaUZ-J&key=AIzaSyAbNu_4U5sh1jXW5VNzAjU3IJSE8encYWY")
	for i in yt_id:
		print i
