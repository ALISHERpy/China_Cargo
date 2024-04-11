from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientModelViewSet, Uzbek_DbModelViewSet, Chine_DbModelViewSet, Available_partyModelViewSet, \
    TrekModelViewSet

router = DefaultRouter()
router.register('Foydalanuvchila', ClientModelViewSet, 'Clients')
router.register('Uzbek_Db', Uzbek_DbModelViewSet, 'Uzbek_DbModelViewSet')
router.register('Chine_Db', Chine_DbModelViewSet, 'Chine_DbModelViewSet')
router.register('Available_partyModelViewSet', Available_partyModelViewSet, 'Available_partyModelViewSet')
router.register('Trek',TrekModelViewSet,"TrekModelViewSet")


urlpatterns = [
    path('', include(router.urls)),
]

