import requests
from django.conf import settings

def aramex(tracking_number):
    # Set the API endpoint and your API key
    api_endpoint = "https://ws.aramex.net/tracking/v2.0/track/ShipmentTracking"
    api_key = "YOUR_API_KEY"
    api_secret = "YOUR_API_SECRET"

    # Set the tracking number for the package you want to track
    tracking_number = "YOUR_TRACKING_NUMBER"

    # Set the request headers
    headers = {
        "Authorization": f"Basic {api_key}:{api_secret}",
        "Content-Type": "application/json",
    }

    # Set the request payload
    payload = {
        "TrackingNumber": tracking_number,
    }

    # Make the request to the API
    response = requests.post(api_endpoint, json=payload, headers=headers)

    # Check the status code of the response
    if response.status_code == 200:
        # If the request was successful, print the tracking information
        tracking_info = response.json()
        return tracking_info
    else:
        # If the request was unsuccessful, print an error message
        return ("An error occurred:", response.text)
