from django.shortcuts import render
from .forms import TodoForm
from users.models import User
from django.http import JsonResponse
from todo.forms import TodoForm
from django.core import serializers

# CATEGORY
def create_todo(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = TodoForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save(commit = False)
            instance.user = request.user
            instance.save()

            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])

            # send to client side.
            return JsonResponse({"instance": ser_instance}, status = 200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status = 400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)