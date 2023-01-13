from youtube_statistics import YTstats
from ETL import ETL


API_KEY = 'AIzaSyBKENtAZHb4HDC8NlyQr9Y5A-RT6rERVb4'
Channel_id = 'UC75V5b1wgQgf0cU_QN6Vw2g'
search = 'yamaha xv750'

file = 'search.json'
destination = 'postgresql://postgres:postgres@localhost:5455/analytics'


yt = YTstats(API_KEY, Channel_id, search)
etl = ETL(file, destination)

#yt.get_channel_statistics()
#yt.get_channel_video_data()
#yt.get_videos_by_search()
#yt.dump()
#yt.dump2()

etl.transform_load()

