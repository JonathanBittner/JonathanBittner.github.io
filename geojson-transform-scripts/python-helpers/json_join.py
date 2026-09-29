import geojson
import sys
from glob import glob



output = sys.argv[1]

args = [f for l in sys.argv[2:] for f in glob(l)]

with open(args[0], 'r') as master:
    geojson_data = geojson.load(master)
    

for arg in args[1:]:
    with open(arg, 'r') as file:
        addData = geojson.load(file)
        for features in addData['features']:
            geojson_data['features'].append(features)
            
            
with open(output, 'w') as out:
    geojson.dump(geojson_data,out)
    
            


