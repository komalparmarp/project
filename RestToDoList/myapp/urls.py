from django.urls import path, include
from .views import TodolistViewset,UserViewset
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('todo', TodolistViewset)
router.register('user',UserViewset)
urlpatterns = [
    path('', include(router.urls)),
]

# ToDo_list = TodolistViewset.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# urlpatterns = [
#     path('', ToDo_list),
# ]
