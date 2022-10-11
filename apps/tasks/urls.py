from django.urls import path, include
from .views import *

urlpatterns = [
    path('tasks/', include([
        path('create/', create, name='create'),
        path('<slug:slug_task>/', include([
            # path('change/', change_task, name="change_task"),
            path("change_status/", change_status, name="change_status"),
            path("delete/", remove_task, name="remove_task"),
        ]))
    ])),
]