import requests
from datetime import datetime
from datetime import timedelta

#own api key
API_key = "your api key"
catalog = 181 #the catalog i used to get the data 

current_datetime = datetime.utcnow()
current_datetime_str = current_datetime.strftime("%Y-%m-%dT%H:%M:%SZ") #the format needed to extract the data
start_time= current_datetime+timedelta(minutes=-3) #can not get the current time's data as it is not always available, thus why I substracted minute(s) from the current time
start_time_str=start_time.strftime("%Y-%m-%dT%H:%M:%SZ")

#defining the start time and end time
parameters = {"start_time": start_time_str, "end_time": current_datetime_str}

# the request template The API key must be added into as HTTP request header, 
# not e.g. into the URL address. If you are importing data from the API into an application, 
#it is usually possible to insert the API key by modifying the request header parameters in your application.
url = 'https://api.fingrid.fi/v1/variable/{}/events/json'.format(catalog)
headers = {'x-api-key': API_key, 'Accept': 'application/json'}
response = requests.get(url, headers=headers, params=parameters)

if response:
    data = response.json() #getting the response from the request

    if data:  #check if there is any data or if the time or anything else is wrong
        value = data[0]['value'] # due to retrieving the data from a json file we retrieve the first value
        timestamp = data[0]['end_time']

        print(f"Current wind power production in Finland: {value} MWh/h")
        print(f"Timestamp: {timestamp}")
    else:
        print("No data available for the specified time.") #in case the time is not right, this will be printed
#else:
  #  print(response.text)
        # i had some issues with errors and i wanted to see what exactly was wrong
