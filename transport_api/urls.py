from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrafficEventViewSet

from transport_api import views
urlpatterns = [
    path('', views.index, name='index'),

    path('simulate/', views.simulation_page),                 # Page HTML
    path('simulate-traffic/', views.simulate_traffic_api),    # API AJAX JS
    path('simulate-traffic-zones/', views.simulate_traffic_per_zone),
    path('best-itinerary/', views.best_itinerary_view),
    path('predict-traffic/', views.predict_traffic_view),
    path('list-transports/', views.list_transports_view),

]


router = DefaultRouter()
router.register(r'events', TrafficEventViewSet)

urlpatterns = router.urls