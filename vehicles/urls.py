from rest_framework import routers
from .views import AirPlaneView, LandVehicleView, BoatView

router = routers.SimpleRouter()
router.register(r'boats', BoatView)
router.register(r'land-vehicles', LandVehicleView)
router.register(r'airplanes', AirPlaneView)
urlpatterns = router.urls