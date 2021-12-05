from rest_framework import routers

from . import viewset

router = routers.DefaultRouter()
router.register("", viewset.ClientViewset, basename="clients")

urlpatterns = router.urls
