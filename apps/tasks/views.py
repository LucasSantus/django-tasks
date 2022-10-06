from .forms import TaskForm
from django.http import JsonResponse
from tasks.forms import TaskForm
from tasks.models import Task
from django.core import serializers
from django.shortcuts import get_object_or_404

# CATEGORY
def create_task(request):
    context = { "error": False, "status": 400 }
    if request.is_ajax and request.method == "POST":
        form = TaskForm(request.POST)
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

def disable_task(request, slug_task):
    task = get_object_or_404(Task, slug = slug_task)
    task.is_active = False
    task.save()

    context = { 
        "status": 200
    }

    return JsonResponse(context)

def remove_task(request, id):
    task = get_object_or_404(Task, id = id)
    task.delete()

    context = { "is_delete": True, "status": 400 }

    return JsonResponse(context)
