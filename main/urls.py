from .views import ShiprecordsView, ShipSpecifivView, TrackingView
from django.urls import path

urlpatterns = [
    path('shipments/<track_no>/', ShipSpecifivView.as_view(), name = "shipment_specific"),
    path('trackers/<track_no>/', TrackingView.as_view(), name = "tracker"),
    path('shipments/', ShiprecordsView.as_view(), name = "shipment")
    
]
