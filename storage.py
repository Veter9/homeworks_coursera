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
new_data = {results.key: [results.val]}

def write_json(data, filename=storage_path):
    with open(filename,'a+') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

write_json(new_data)


with open(storage_path) as json_file:
        old_data = json.load(json_file)

def extract_values(obj, key):
    """Recursively pull values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Return all matching values in an object."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results



if results.val == None:
    if results.key in old_data:
        print("exist")
        a = results.key
        print(results.key)
        print(a)
        print("--------------")
        # for element in old_data[results.key]:
        #     print(element[0], "," element[1])    

    else:
        print(None)
else:
    with open(storage_path) as json_file:
        old_data = json.load(json_file)
        new_data.update(old_data)
        json_file.seek(0)
    os.remove(os.path.join(tempfile.gettempdir(), "storage.data"))   
    write_json(new_data)   