import requests
from django.conf import settings

def dhl(awb_number):
    # Set the API endpoint and your API key
    api_endpoint = f"https://api-eu.dhl.com/track/shipments?trackingNumber={awb_number}"

    # Set the tracking number for the package you want to track
    tracking_number = awb_number

    # Set the request headers
    headers = {
        "DHL-API-Key": settings.API_KEY_DHL,
        "Content-Type": "application/json",
    }

    # Set the request payload
    payload = {
        "trackingNumber": tracking_number,
    }

    # Make the request to the API
    response = requests.get(api_endpoint,headers=headers)

    # Check the status code of the response
    if response.status_code == 200:
        # If the request was successful, print the tracking information
        tracking_info = response.json()
        info_tracking = {"Data": []}
        for i in tracking_info["shipments"][0]["events"]:
            info_tracking["Data"].append({
                'ShipDate':i['timestamp'],
                'Status':i['location']['address']['addressLocality'],
                'Remarks':i['description']
            })            
        return info_tracking
    
    else:
        # If the request was unsuccessful, print an error message
        print(response)
        return response.text