from django.urls import path
from rest_framework import routers
from .views import SimViewSet


router = routers.DefaultRouter()
router.register('simulation', SimViewSet)

urlpatterns = router.urls

# from .views import index 


# urlpatterns = [
#     path('simulation/', index)
# ]