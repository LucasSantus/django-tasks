from django.db import models
from core.models import BaseModel
from autoslug import AutoSlugField
import random
from django.http import JsonResponse

# Create your models here.
class Task(BaseModel):
    title = models.CharField(verbose_name = "Título", max_length = 100)
    description = models.TextField(verbose_name = "Descrição")
    slug = AutoSlugField(populate_from = 'generated_slug_title', unique_with = [ 'title' ], unique = True, editable = True)
    user = models.ForeignKey("accounts.User", on_delete = models.CASCADE, related_name="user_todos")

    def generated_slug_title(self):
        return f"{self.title}-{random.randint(1, 9999)}"

    def deactivate_task(self):
        return reverse('task:deactivate', args=[str(self.slug)])

    class Meta:
        verbose_name = "Tarefas"
        verbose_name_plural = "Tarefa"
        db_table = "tasks"
        app_label = "tasks"

    def __str__(self):
        return self.title