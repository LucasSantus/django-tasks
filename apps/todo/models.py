from django.db import models
from core.models import BaseModel
from autoslug import AutoSlugField

# Create your models here.
class Todo(BaseModel):
    title = models.CharField(verbose_name = "Título", max_length = 100, unique = True)
    slug = AutoSlugField(populate_from = 'title', unique_with = [ 'title' ], unique = True, editable = True)
    user = models.ForeignKey("users.User", on_delete = models.CASCADE, related_name="user_todos")

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
        db_table = "todos"
        app_label = "todo"

    def __str__(self):
        return self.get_full_name()
