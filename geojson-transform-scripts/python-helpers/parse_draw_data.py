#for use with data from drawonamap.com
#I can draw a point for a route shield and label it, but the label text is not accessible to Mapbox
import geojson
import sys
import json

#ouptut file name
output = sys.argv[2]

with open(sys.argv[1], 'r') as file:   
    addData = geojson.load(file)
    for features in addData['features']:
        drawString = features["properties"]["drawonamapDrawing"]
        print(drawString)
        drawData = json.loads(drawString)
        ref=drawData["text"]
        print(ref)
        features["properties"]["ref"] = ref
        
            
with open(output, 'w') as out:
    geojson.dump(addData,out)