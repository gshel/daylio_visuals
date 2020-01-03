import csv
import os
from datetime import datetime

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import RequestError
from tqdm import tqdm

# where to GET your data
daylio_export_name = 'daylio_export.csv'
if os.path.isfile(daylio_export_name):
    pass
else:
    print(f"Unable to find '{daylio_export_name}' in {os.getcwd()}. Fix this, then try again.")
    exit(1)

csvfilepath = open(daylio_export_name, 'r', encoding='utf-8')
print(f"Found and accessed '{csvfilepath.name}'")

# where to PUT your data
es = Elasticsearch('http://localhost:9200/')
print(f"Connected to Elasticsearch on {es.cluster.client}")

# don't duplicate any existing data by deleting and starting fresh
index_name = 'daylio'
if es.indices.exists(index=[index_name]):
    es.indices.delete(index=index_name)
    print(f"Deleted existing '{index_name}' index")
es.indices.create(index=index_name)
print(f"Created sparkly, new '{index_name}' index")

# process each row/entry in the csv
reader = csv.DictReader(csvfilepath)
print(f"Reading '{csvfilepath.name}'...")

for row in tqdm(reader):
    full_date = [key for key in row.keys() if "full_date" in key][0]

    # combine full date and time
    date = datetime.strptime(row[full_date], '%Y-%m-%d')
    time = datetime.strptime(row['time'], '%H:%M').time()
    datetime_obj = datetime.combine(date, time).isoformat()
    row['datetime'] = datetime_obj

    # make a boolean key for each activity listed
    for activity in row['activities'].split(' | '):
        row[activity] = True

    # delete unnecessary keys
    for i in [full_date, 'date', 'weekday', 'time', 'activities']:
        row.pop(i)

    # insert each row from the CSV into Elasticsearch as a document, so that we can visualize it using Kibana
    try:
        es.index(index='daylio', doc_type='json', body=row)
    except RequestError:
        print(f"ERROR! Unable to index malformed row:\n{row}")
        pass

csvfilepath.close()
print(f"Go to Kibana at 'http://localhost:5601' in your browser")
