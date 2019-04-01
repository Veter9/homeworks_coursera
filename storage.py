import os
import tempfile
import argparse
import json
import tempfile
#waiting for new variables to input 
parser = argparse.ArgumentParser()
parser.add_argument('--key', action='store', dest='key', help='key')
parser.add_argument('--val', action='store', dest='val', help='value')
results = parser.parse_args()
#vars

data = {}  
data['store1'] = []  
data['store1'].append({  
    results.key: results.val
})

with open('data.txt', mode='a+') as json_file:
    json_file = {results.key: results.val}
    json.dump(data, json_file)
  
with open('data.txt') as json_file:  
    data = json.load(json_file)
    for p in data['store1']:
        print(results.key + p[results.key])


# if results.val == None:
#     with open(storage_path, 'r+') as f:
#         # print(f.read())
#         print("1")
# else:
#     with open(storage_path, 'r+') as f:
#         # f.write(results.key)
#         # f.seek(0)
#         print("2")

