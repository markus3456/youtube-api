from youtube_statistics import YTstats


Channel_id = 'UC75V5b1wgQgf0cU_QN6Vw2g'

yt = YTstats(API_KEY, Channel_id)
yt.get_channel_statistics()
yt.dump()

