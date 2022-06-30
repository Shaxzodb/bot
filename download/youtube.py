# from cv2 import split
# import requests
import pprint
# url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"

# querystring = {"id":"oNyaiWgqKDI","geo":"DE"}

# headers = {
# 	"X-RapidAPI-Key": "f35d2d07c9msha9151ff2cbccd21p1f4244jsn171519496d16",
# 	"X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# pprint.pprint(response.json()['link']['134'][0])

import logging
import requests
# Tiktok video yuklash
async def youtube(message):
    
    try:
        url ="https://ytstream-download-youtube-videos.p.rapidapi.com/dl"
        text=message.text.split("=")
        print(text[1])
        querystring = {"id":f'{text[1]}',"geo":"DE"}

        headers = {
            "X-RapidAPI-Key": "f35d2d07c9msha9151ff2cbccd21p1f4244jsn171519496d16",
	        "X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
	        
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        
        
        #await message.answer_video(video = response.json()["link"]["134"][0])
        pprint.pprint(response.json()['link']['18'][0])
        await message.answer_video(video=response.json()['link']['18'][0])
        
    except Exception as error:
        
        #await message.answer('<b>{}</b> - tiktok video yuklanmadi qaytib link ni tug\'riligini tekshirib ko\'ring'.format(message.text))
        await message.answer('<b>{}</b> - tiktok video tehnik sabablarga kura yuklanmadi buning uchun uzur suraymiz, botda tuzatish ishlari olib borilyapti tez orada bu xato tuzatiladi'.format(message.text))
        logging.error(f'Tiktok File: {error}')

#os.getenv('YHOST'),os.getenv('KEY'),os.getenv('YURL')