from youtube_statistics import YTstats

API_KEY = 'AIzaSyBKENtAZHb4HDC8NlyQr9Y5A-RT6rERVb4'
Channel_id = 'UC75V5b1wgQgf0cU_QN6Vw2g'
search = 'yamaha xv750'

yt = YTstats(API_KEY, Channel_id, search)

#yt.get_channel_statistics()
#yt.get_channel_video_data()
yt.get_videos_by_search()
yt.dump()
#yt.get_channel_video_data()

