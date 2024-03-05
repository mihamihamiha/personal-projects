from XmlToJson.Transformxmltojson.transformxmltojson import transform
import json

def test_transform():
    testfile = r"XmlToJson\unittest\datatest.xml"
    transform(testfile,"test.json")
    with open("test.json") as file:
        result = json.load(file)
    assert result == {
        "Documents": {
            "Document": 
                {
                    "title": "Annual Report 2023",
                    "filename": "Annual_Report_2023.pdf",
                    "filesize": "5MB",
                    "file-extension": "pdf",
                    "owner": "John Doe",
                    "create_timestamp": "2023-03-01T12:00:00",
                    "modified_timestamp": "2023-03-05T15:30:00",
                    "retention_period": "5 years",
                    "organisation": "ABC Corporation",
                    "department": "Finance"
                }
        }
    }
    #print(result)
    #for when the test was failing (it was because of me :( )

    #reminder for self: run python -m pytest to test it!!