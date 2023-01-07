from youtube_statistics import YTstats

API_KEY = 'AIzaSyBKENtAZHb4HDC8NlyQr9Y5A-RT6rERVb4'
Channel_id = 'UC75V5b1wgQgf0cU_QN6Vw2g'

yt = YTstats(API_KEY, Channel_id)
yt.get_channel_statistics()
yt.get_channel_video_data()
yt.dump()
#yt.get_channel_video_data()

