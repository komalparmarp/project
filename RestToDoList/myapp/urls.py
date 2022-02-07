from django.urls import path, include
from .views import TodolistViewset,UserViewset
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
router = DefaultRouter()

router.register('todo', TodolistViewset)
router.register('user',UserViewset)
urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),

]

# ToDo_list = TodolistViewset.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# urlpatterns = [
#     path('', ToDo_list),
# ]
