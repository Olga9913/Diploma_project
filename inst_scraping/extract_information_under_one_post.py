# bot.login(username = 'xxx',  password = 'xxx')

import requests
import json
import re


headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}

r = requests.get('https://www.instagram.com/p/CESHVluh80t/', headers=headers)

script = re.search(r'window._sharedData = (.+?);</script>', r.text).group(1)
data = json.loads(script)

edges = data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_caption']['edges']
for edge in edges:

    text = edge['node']['text']
    #author = edge['node']['owner']['username']

    print(text)



