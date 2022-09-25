from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ("title", "description")

        # error_messages = {
        #     "title":{
        #         "required": "Insira o título da categoria!",
        #         "invalid": "Insira um título válido!"
        #     },
        #     "description":{
        #         "required": "Insira a descrição da categoria!",
        #         "invalid": "Insira uma descrição válida!"
        #     },
        # }