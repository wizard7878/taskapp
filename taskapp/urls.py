from django.urls import path
from .views import ListContentViewSet, CreateRateContentViewSet

urlpatterns = [
    path('content/', ListContentViewSet.as_view({'get': 'list'})),
    path('content/rate/<int:content_id>', CreateRateContentViewSet.as_view({'post': 'create'}))
]