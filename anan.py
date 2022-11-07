import requests
import time
from TikTokAPI import TikTokAPI
from instagrapi import Client


cl = Client()
cl.login("username", "password")

cookie = {
  "s_v_web_id": "verify_l66b0yrg_dkYVKdNX_Clcw_4R6A_AhcY_vVavmOLQIrPz",
  "ttwid": "1%7CRpsm40KxZl4Okl27i58IMzvh7SsWorzJNRasjF5XuOs%7C1659089494%7Cc1a732807230f168f556775a406956d70d049391987e04465fbecef79e27dfc8"
}



while True:
         time.sleep(1000)
         api = TikTokAPI(language='tr', cookie=cookie)
         retval = api.getTrending(count=1)
        
         api.downloadVideoById(retval['items'][4]['id'],  f"{retval['items'][4]['createTime']}.mp4")
         media = cl.clip_upload(f"./{retval['items'][4]['createTime']}.mp4", f"| {retval['items'][3]['desc']}",     extra_data={
                 "custom_accessibility_caption": "alt text example",
                 "like_and_view_counts_disabled": 0,
                 "disable_comments": 0,
             }
         )

         print("Başarıyla yüklendi! ")