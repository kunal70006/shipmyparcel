from ..models import Tracker
import requests
from django.http import HttpResponse
from rest_framework.views import APIView
import json
from ..serializer import TrackerSerializer
from . import aramexview, fedexview,upsview,dhlview,skynetview
import random

class ShiprecordsView(APIView):
    def get(self,request):
        user = request.user
        print(user)
        trackers = Tracker.objects.all()
        serializer = TrackerSerializer(trackers, many=True)
        data = serializer.data[:]
        return HttpResponse(json.dumps(data), content_type="application/json")
    

    def post(self, request):
        resp = {"value": ""}
        
        #tracking number generator
        digits = [str(random.randint(0, 9)) for _ in range(8)]
        tracking_no =  "smp" + "".join(digits)
        
        data = {
            "tracking_no": tracking_no,
            "awb_no": request.data['awb_no'],
            "delivery_server": request.data['delivery_server']
        }
        try:
            c = Tracker.objects.create(tracking_no = data['tracking_no'], awb_no = data['awb_no'], delivery_server = data['delivery_server'])
            c.save()
            resp["tracking_no"] = tracking_no
        except:
            resp["value"] = "failed"
        return HttpResponse(json.dumps(resp), content_type="application/json")
    
    
class ShipSpecifivView(APIView):
    def put(self, request, track_no):
        resp = {'status':'failed'}
        tracker = Tracker.objects.filter(tracking_no = track_no).first()
        serializer = TrackerSerializer(tracker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json.dumps(serializer.data), content_type="application/json")
        return HttpResponse(json.dumps(resp), content_type="application/json")

    def delete(self, request, id):

        resp = {'status':''}
        try:
            Tracker.objects.filter(id = id).delete()
            resp['status'] = 'success'
        except:
            resp['status'] = 'failed'
        return HttpResponse(json.dumps(resp), content_type="application/json")
    
    
class TrackingView(APIView):
    def get(self,request, track_no):

        # try:
        tracker = Tracker.objects.get(tracking_no= track_no)
        
        response = {'status': 'failed'}
        
        print(tracker.delivery_server)
        if tracker.delivery_server == "fedex":
            response = fedexview.fedex(tracker.awb_no)
        elif tracker.delivery_server == "dhl":
            response = dhlview.dhl(tracker.awb_no)
            
        elif tracker.delivery_server == "aramex":
            response = aramexview.aramex(tracker.awb_no)
        
        elif tracker.delivery_server == "ups":
            response = upsview.ups(tracker.awb_no)
            
        elif tracker.delivery_server == "skynet":
            response = skynetview.skynet(tracker.awb_no)
            
        return HttpResponse(json.dumps(response), content_type="application/json")
        # except:
        return HttpResponse(json.dumps(response), content_type="application/json")
    
    
# fedex skynet dhl ups aramex dpd uk
# https://api.skynet.com.my/api/sn/pub/AWBTracking/





