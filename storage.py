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

new_data = {results.key: [results.val]}
print(new_data)
print("1111111111111111111")
json_view = json.dumps(new_data, sort_keys=True, indent=4)
print(json_view)
print("2222222222222222222")
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

with open(storage_path) as json_file:
    old_data = json.load(json_file)
    
print(old_data)

if results.key in old_data:
    print("exist")
    print(results.val)
else:
    print("not exist")
    with open(storage_path, 'a+') as d:
        d.write(new_data)
        d.close()

