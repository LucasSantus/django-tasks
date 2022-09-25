from django.db import models
import json
from django.core.serializers.json import DjangoJSONEncoder

def convert_object_in_json(item):
    return json.dumps(list(item), cls = DjangoJSONEncoder)

class BaseModel(models.Model):
    is_active = models.BooleanField(verbose_name = "Ativo", default = True)
    create_at = models.DateTimeField(verbose_name = "Data & Hora registrado", auto_now_add = True)
    update_at = models.DateTimeField(verbose_name = "Data & Hora modificado", blank = True, null = True, editable = True)
    desactivate_at = models.DateTimeField(verbose_name = "Data & Hora desativado", blank = True, null = True, editable = True)

    class Meta:
        abstract = True