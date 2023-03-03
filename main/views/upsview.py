import requests

def ups(tracking_number):
    # Set the API endpoint and your API key
    api_endpoint = "https://wwwcie.ups.com/rest/Track"
    api_key = "YOUR_API_KEY"

    # Set the tracking number for the package you want to track
    tracking_number = "YOUR_TRACKING_NUMBER"

    # Set the request headers
    headers = {
        "Access License Number": api_key,
        "Content-Type": "application/json",
    }

    # Set the request payload
    payload = {
        "InquiryNumber": tracking_number,
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
        return response.text