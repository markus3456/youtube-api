import requests 
import json

class YTstats:

    def __init__(self, api_key, Channel_id):
        self.api_key = api_key
        self.channel_id = Channel_id
        self.channel_statistics = None

    def get_channel_statistics(self):
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}'
        #print(url)
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        
        try:
            data = data["items"][0]["statistics"]
        except: 
            data = None
        
        self.channel_statistics = data
        return data

    def dump(self):
        if self.channel_statistics is None:
            return

        channel_title = "Racer TV"
        channel_title = channel_title.replace(" ", "_").lower()
        file_name = channel_title + '.json'
        with open(file_name, 'w') as f:
            json.dump(self.channel_statistics, f, indent=4)
        
        print('file dumped')

    #get_channel_statistics()