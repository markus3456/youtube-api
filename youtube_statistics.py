import requests 
import json




class YTstats:

    def __init__(self, api_key, Channel_id, search):
        self.api_key = api_key
        self.channel_id = Channel_id
        self.channel_statistics = None
        self.video_data = None
        self.search = search

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

    def get_channel_video_data(self):
        # 1. get video ids
        channel_videos = self._get_channel_videos(limit=50)
        print(channel_videos)
        print(len(channel_videos))
      
        #2. get vidoe statistics
        parts = ["snippet","statistics","contentDetails"]
        for video_id in channel_videos:
            for part in parts:
                data = self._get_single_video_data(video_id, part)
                channel_videos[video_id].update(data)
        
        self.video_data = channel_videos
        return channel_videos

    def _get_single_video_data(self, video_id, part):
        url = f'https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={self.api_key}'
        #print(url)
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try: 
            data = data['items'][0][part]
        except:
            print('error')
            data = dict()
        
        return data


    def  _get_channel_videos(self, limit=None):
        url = f'https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&part=id&order=date'
        if limit is not None and isinstance(limit, int):
            url += "&maxResults" + str(limit)
        
        vid, npt = self._get_channel_videos_per_page(url)
        idx = 0
        while(npt is not None and idx < 10):
            nexturl = url + "&pageToken=" + npt
            next_vid, npt = self._get_channel_videos_per_page(nexturl)
            vid.update(next_vid)
            idx +=  1

        return vid

    def _get_channel_videos_per_page(self, url):
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        channel_videos = dict()
        if 'items' not in data:
            return channel_videos, None
        
        item_data = data['items']
        nextPageToken = data.get("nextPageToken", None)
        for item in item_data:
            try:
                kind = item['id']['kind']
                if kind == 'youtube#video':
                    video_id = item['id']['videoId']
                    channel_videos[video_id] = dict()
            except KeyError:
                print("Key error")
        
        return channel_videos, nextPageToken

    def get_videos_by_search(self, limit=50):
        #1. get vidoe ids
        searched_videos = self._get_search_video_id(limit=50)
        print(searched_videos)
        print(len(searched_videos))
        
        #2. get video statistics
        parts = ["snippet","statistics","contentDetails"]
        for video_id in searched_videos:
            for part in parts:
                data = self._get_single_video_data(video_id, part)
                searched_videos[video_id].update(data)
        
        self.video_data = searched_videos
        return searched_videos
    
    def _get_search_video_id(self, limit):
        url =f'https://www.googleapis.com/youtube/v3/search?key={self.api_key}&q={self.search}'
        print(url)
        if limit is not None and isinstance(limit, int):
            url += "&maxResults" + str(limit)

        vid, npt = self._get_channel_videos_per_page(url)
        idx = 0

        while(npt is not None and idx < 10):
            nexturl = url + "&pageToken=" + npt
            next_vid, npt = self._get_channel_videos_per_page(nexturl)
            vid.update(next_vid)
            idx +=  1

        return vid

    def _get_search_videos(self, url):
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        searched_videos = dict()
        if 'items' not in data:
            return searched_videos, None
        
        item_data = data['items']
        nextPageToken = data.get("nextPageToken", None)
        for item in item_data:
            try:
                kind = item['id']['kind']
                if kind == 'youtube#video':
                    video_id = item['id']['videoId']
                    searched_videos[video_id] = dict()
                    print(video_id)
            except KeyError:
                print("Key error")
        
        return searched_videos, nextPageToken


    def dump(self):
        if self.channel_statistics is None or self.video_data is None:
            print('data is none')
            return
        
        
        fused_data = {self.channel_id: {"channel_statistics": self.channel_statistics, "video_data": self.video_data}}

        channel_title = self.video_data.popitem()[1].get('channelTitle', self.channel_id)
        channel_title = channel_title.replace(" ", "_").lower()
        file_name = channel_title + '.json'
        with open(file_name, 'w') as f:
            json.dump(fused_data, f, indent=4)
        
        print('file dumped')

    def dump2(self):
        if self.video_data is None:
            print("data is none")
            return
        
        #fused_data = {self.channel_id: {"channel_statistics": self.channel_statistics, "video_data": self.video_data}}

        file_name = 'search.json'
        with open(file_name, 'w') as f:
            json.dump(self.video_data, f, indent=4)
        
        print('file dumped')
