import fedex
from django.conf import settings

def fedex(awb_number):
        
    client = fedex.FedEx(key= settings.api_key_fedex, password=settings.password_fedex, account_number=settings.account_number_fedex, meter_number=settings.meter_number.fedex, use_test_server=True)

    tracking_request = fedex.TrackRequest(tracking_number=awb_number)
    
    tracking_response = client.send_request(tracking_request)

    
    tracking_info = tracking_response.TrackDetails[0]
    status = tracking_info.StatusDescription
    delivery_date = tracking_info.DeliveryTimestamp

    
    return tracking_response
