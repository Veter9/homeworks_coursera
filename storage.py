import os
import tempfile
import argparse
import json
import tempfile
#waiting for new variables to input 
parser = argparse.ArgumentParser()
parser.add_argument('--key', action='store', dest='key', help='key')
parser.add_argument('--val', nargs='+', action='store', dest='val', help='value')
results = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def write_json(data, filename=storage_path):
    with open(filename,'a+') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

new_data = {results.key: [results.val]}

with open(storage_path) as json_file:
        old_data = json.load(json_file)


if results.val == None:
    if results.key in old_data:
        print("exist")
        for key, value in old_data.items():
            print(value)

    else:
        print(None)
else:
    with open(storage_path) as json_file:
        old_data = json.load(json_file)
        new_data.update(old_data)
        json_file.seek(0)
    os.remove(os.path.join(tempfile.gettempdir(), "storage.data"))   
    write_json(new_data)   