from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from . import views

router = DefaultRouter()
router.register('hogehoge', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('index/<int:id>/', views.index, name='index'),
    path('get/<int:id>/', views.index_get, name='index_get'),
    path('getall/', views.index_get_all, name='index_get_all'),
    path('post/<str:name>/<int:price>/', views.index_post, name='index_post'),
    path('patch/<int:id>/<str:name>/<int:price>/', views.index_patch, name='index_patch'),
    path('delete/<int:id>/', views.index_delete, name='index_delete'),
]