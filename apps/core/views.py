from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import convert_object_in_json
from tasks.forms import TaskForm

def error_404(request, exception):
    return render(request, '404.html', status = 404)

@login_required
def index(request):
    # tasks = Task.objects.prefetch_related("user").filter( user = request.user, is_active = True ).values()
    tasks = Task.objects.prefetch_related("user").filter( user = request.user ).values()

    form = TaskForm()

    context = {
        "tasks": convert_object_in_json(tasks),
        'form': form
    }

    return render(request, 'core/index.html', context)