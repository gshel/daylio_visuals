import csv
from datetime import datetime

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import RequestError

print("Starting...")
# where to GET your data
csvfilepath = 'daylio_export.csv'
print(f"Successfully accessed {csvfilepath}")

print("Connecting to Elasticsearch...")
# where to PUT your data
es = Elasticsearch('http://localhost:9200/')
print(f"Successfully connected to 'http://localhost:9200/'")

# delete the existing Daylio index so that we don't insert duplicate data
if es.indices.exists(index=["daylio"]):
    print("Deleting existing 'daylio' index...")
    es.indices.delete(index="daylio")

print("Creating a new 'daylio' index...")
# create a new, blank Daylio index
es.indices.create(index="daylio")

# iterate over the data in csvfilepath (your Daylio export)
reader = csv.DictReader(open(csvfilepath, 'r', encoding='utf-8'))
print(f"Successfully reading {csvfilepath}, beginning to index each row now...")
for row in reader:
    # combine full date and time
    date = datetime.strptime(row['''\ufefffull_date'''], '%Y-%m-%d')
    time = datetime.strptime(row['time'], '%H:%M').time()
    datetime_obj = datetime.combine(date, time).isoformat()
    row['datetime'] = datetime_obj

    # delete unnecessary keys
    row.pop('''\ufefffull_date''')
    row.pop('date')
    row.pop('weekday')
    row.pop('time')

    # Make a boolean key for each activity listed
    for activity in row['activities'].split(' | '):
        row[activity] = True

    # delete the activities key because we processed them in the for-loop just above this comment
    row.pop('activities')

    # insert each row from the CSV into Elasticsearch as a document, so that we can visualize it using Kibana
    try:
        es.index(index='daylio', doc_type='json', body=row)
    except RequestError:
        print(f"ERROR! Unable to index malformed row:\n{row}")
        pass
print("Finished indexing all rows into Elasticsearch.\nGo to 'http://localhost:5601' in your browser.")
