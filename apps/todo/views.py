from django.shortcuts import render
from .forms import TodoForm
from users.models import User
from django.http import JsonResponse
from todo.forms import TodoForm
from django.core import serializers

# CATEGORY
def create_todo(request):
    context = { "error": None, "status": 400 }
    
    if request.is_ajax and request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            data = form.save(commit = False)
            data.user = request.user
            data.save()
            
            data_serialized = serializers.serialize('json', [ data ])

            context = { "data": data_serialized, "status": 200 }

            # return JsonResponse({ "data": data_serialized }, status = 200)
        else:
            
            context = { "error": form.errors, "status": 400 }
            # return JsonResponse({ "error": form.errors }, status = 400)

    return JsonResponse(context)