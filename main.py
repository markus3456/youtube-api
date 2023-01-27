from youtube_statistics import YTstats
from ETL import ETL



Channel_id = 'UC75V5b1wgQgf0cU_QN6Vw2g'
search = 'honda cb750'

file = 'search.json'
destination = 'postgresql://postgres:postgres@localhost:5455/analytics'


yt = YTstats(API_KEY, Channel_id, search)


#yt.get_channel_statistics()
#yt.get_channel_video_data()
yt.get_videos_by_search()
#yt.dump()
yt.dump2()

etl = ETL(file, destination)
etl.transform_load()

