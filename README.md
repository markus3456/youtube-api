**ETL from youtube-api to PosgresDB hosted by Docker-Container**

**Extract**

The Program is using googleapi-urls to scrap data from youtube and saves it as a json file with the API-Key provided.
output is a jsonfile with information about videos including sats such as view count, likes, comments 

**Transform**

Data is transformed from json to pandas DataFrame with the relevant filtered information 
data is transformed to .csv

**load**

filtered data is uploaded to Postgres-Database using psycopg2


provide API_KEY to connect to youtube-API
provide searchkeyword or channelID to extract the statistical data of videos you are interested in
provide destination location of database to upload the the extracted and transformed data


