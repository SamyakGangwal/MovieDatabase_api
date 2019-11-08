
from django.urls import path,include
from . import views 
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('movie', views.movieView)
router.register('watch',views.watchView)
router.register('popular',views.polularView)
router.register('latest',views.latestView)

urlpatterns = [

    path('',include(router.urls)),
    path('api/token', TokenObtainPairView.as_view()),
	path('api/token/refresh', TokenRefreshView.as_view())    
    
]
