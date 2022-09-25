from django.urls import path, include
from .views import *

urlpatterns = [
    path('todos/', include([
        path('create/', create_todo, name='create_todo'),
        path('<slug:slug_todo>', include([
            path('change/', change_todo, name="change_todo"),
            path("delete/", delete_todo, name="delete_todo"),
        ]))
    ])),
]