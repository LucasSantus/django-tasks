from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from todo.models import Todo
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import convert_object_in_json
from todo.forms import TodoForm

def error_404(request, exception):
    return render(request, '404.html', status = 404)

@login_required
def index(request):
    todos = Todo.objects.prefetch_related("user").filter(user = request.user).values()

    form = TodoForm()

    context = {
        "todos": convert_object_in_json(todos),
        'form': form
    }

    return render(request, 'core/index.html', context)