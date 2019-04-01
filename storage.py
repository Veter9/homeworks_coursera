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

input_first = json.dumps({results.key: results.val}, sort_keys=True, indent=4)

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


if results.val == None:
    with open(storage_path, 'r+') as f:
        f.seek(0)
        print(f.read())

else:
    with open(storage_path, 'r+') as f:
        f.write(input_first)

