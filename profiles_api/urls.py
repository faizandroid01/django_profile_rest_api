from django.urls import path , include
from rest_framework.routers import DefaultRouter
from profiles_api import views

# To add distinct functionalities of viewset in url mapping
router =  DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, basename = 'hello-viewset')

urlpatterns = [
  path('hello-view/', views.HelloApiView.as_view()),
  path('',include(router.urls)),
]