from django.urls import path, include
from .views import *

urlpatterns = [
    path('tasks/', include([
        path('create/', create_task, name='create_task'),
        path('<slug:slug_task>', include([
            # path('change/', change_task, name="change_task"),
            path("delete/", remove_task, name="remove_task"),
        ]))
    ])),
]