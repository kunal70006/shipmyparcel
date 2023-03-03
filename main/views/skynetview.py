import requests
from django.conf import settings

def skynet(awb_number):
    # Set the API endpoint and your API key
    # api_endpoint = "https://api.skynet.com.my/api/sn/pub/AWBTracking/"
    # api_endpoint =  "https://services.skynetww.com/api/Skynet/SkynetGetOnline"
    api_endpoint =  "https://services.skynetww.com/api/Skynet/GetShipmentHistory"
    
    

    # Set the tracking number for the package you want to track
    tracking_number = awb_number

    # Set the request headers
    headers = {
        "Content-Type": "application/json",
        "Username": "SKY@A018",
        "password": "LOGIN@A018",
        "Acesskey": "SKY@2022" 

    }

    # Set the request payload
    payload = {
         "Awbno":tracking_number,   
    }

    # Make the request to the API
    response = requests.post(api_endpoint, json=payload, headers=headers)

    # Check the status code of the response
    if response.status_code == 200:
        # If the request was successful, print the tracking information
        tracking_info = response.json()
        info_tracking = {"Data":[]}
        for i in tracking_info["Data"]:
            info_tracking["Data"].append(i)
        return info_tracking
    
    else:
        # If the request was unsuccessful, print an error message
        return response.text