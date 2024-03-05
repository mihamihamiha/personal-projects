import xmltodict
import json

def transform(data,exitfile):
    with open(data) as file:
        data2=xmltodict.parse(file.read())
        with open(exitfile, "w") as file2:
            json.dump(data2,file2,indent=2)
            
transform("XmlToJson\Transformxmltojson\data.xml","data.json")