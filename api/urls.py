from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()

router.register(r'company', views.CompanyViewSet, basename='company')
router.register(r'jobpost', views.JobPostViewSet, basename='jobpost')
router.register(r'user', views.UserViewSet, basename='user')
router.register(r'application', views.ApplicationViewSet, basename='application')
router.register(r'search', views.SearchKeywordkViewSet, basename='search')

urlpatterns = [
    path('', include(router.urls)),
]
