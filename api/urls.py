from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()

router.register(r'company', views.CompanyViewSet)
router.register(r'jobpost', views.JobPostViewSet, basename='jobpost')
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
