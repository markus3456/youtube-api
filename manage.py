import psycopg2
from ETL import ETL

destination = 'postgresql://postgres:postgres@localhost:5455/analytics'

def create_db(destination):
    #connect to database
    conn_string = destination
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print('opend db successfully')
    
    #drop existing tables
    cursor.execute("drop table if exists racerdata;")

    #create table
    cursor.execute("create table racerdata \
        (titel varchar, video_id varchar, views float, likes float, comments float)")

create_db(destination)

