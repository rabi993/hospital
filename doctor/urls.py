from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()
router.register('list', views.DoctorViewset)
router.register('specialization', views.SpecializationViewset)
router.register('designation', views.DesignationViewset)
router.register('availableTime', views.AvailableTimeViewset)

urlpatterns = [
    path('', include(router.urls)),
]