import sys
import json
import pprint as pp


file_name = sys.argv[1]
route_ref = sys.argv[2]

print("writing \"" + route_ref + "\" to file: " + file_name)

with open(file_name, 'r+') as file:
    #strip off the wikipedia layer
    payload = json.load(file)
    data = payload['data']
    #print(data)
    #geojson_data = geojson.load(file)
    
    for features in data['features']:
        features["properties"]["ref"] = route_ref
    
    file.seek(0)
    json.dump(data, file)
    file.truncate()

    