from django.urls import path
from tracking.views import TrackingViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tracking/playhub', TrackingViewSet)
# router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls
