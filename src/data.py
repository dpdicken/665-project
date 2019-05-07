import json
from collections import defaultdict
from datetime import datetime

def parse_date_time(date_time_str):
    date_time_obj = datetime.strptime(date_time_str, "%a %b %d %H:%M:%S %z %Y")
    return date_time_obj

def read_json_data_file(filename):
    objs = defaultdict(lambda: [])
    with open(filename, errors='replace') as file:
        for line in file:
            item = json.loads(line)
            new_item = {
                "text" : item['text'],
                "time" : parse_date_time(item['created_at'])
            }
            objs[item['user']['id']].append(new_item)
    return objs
