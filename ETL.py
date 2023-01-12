import pandas as pd
import json
import psycopg2

def test_db_connection():
    conn_string = 'postgresql://postgres:postgres@localhost:5455/analytics'
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print('opend db successfully')

#test_db_connection()

def transform(fjson):

    file = fjson
    data = None
    with open(file, 'r') as f:
        data = json.load(f)

    video_stats = data

    sorted_vids = sorted(video_stats.items(), key=lambda item: int(item[1]["viewCount"]), reverse=True)
    stats = []
    for vid in sorted_vids:
        video_id = vid[0]
        title = vid[1]["title"]
        views = int(vid[1]["viewCount"])
        likes = int(vid[1].get("likeCount",0))
        comments = int(vid[1].get("commentCount",0))
        stats.append([title,views,likes,comments])

    df = pd.DataFrame(stats, columns=["title","views","likes","comments"])
    print(df.head(10))
    return(df)

def load(df):
    #replace df data types with sql datatypes
    replacements = {
        'object': 'varchar',
        'float64': 'float',
        'int64': 'int',
        'datetime64[ns]': 'timestamp',
        'timedelta64[ns]': 'varchar'
    }
    print(replacements)

    col_str = ", ".join("{} {}".format(n,d) for (n,d) in zip(df.columns, df.dtypes.replace(replacements)))
    print(col_str)

    #connect to database
    conn_string = 'postgresql://postgres:postgres@localhost:5455/analytics'
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print('opend db successfully')
    
    #drop existing tables
    cursor.execute("drop table if exists racerdata;")

    #create table
    cursor.execute("create table racerdata \
        (titel varchar, views float, likes float, comments float)")

    #insert values to table by saving df to csv in temp folder and upload to db
    df.to_csv('racerdata.csv', header=df.columns, index=False, encoding='utf-8')
    my_file = open('racerdata.csv', encoding="utf8")

    SQL_STATEMENT = """
    COPY racerdata FROM STDIN WITH
    CSV
    HEADER
    DELIMITER AS ','
    """
    cursor.copy_expert(sql=SQL_STATEMENT, file=my_file)
    cursor.execute("grant select on table racerdata to public")
    conn.commit()

    cursor.close()
    print('upload complete')
    print(len(df.index))

file = 'search.json'
df = transform(file)
load(df)
