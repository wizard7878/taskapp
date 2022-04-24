from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import SignUpViewSet


urlpatterns = [
    path('signup/', SignUpViewSet.as_view({'post': 'create'})),
    path('signin/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]