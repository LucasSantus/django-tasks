from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.urls import reverse
from core.models import BaseModel

class UserManager(BaseUserManager):
    def create_user(self, full_name, email, password = None, **kwargs):
        if not full_name: raise ValueError('Insira um nome para continuar!')
        if not email: raise ValueError('Insira um e-mail para continuar!')

        user = self.model(
            full_name = full_name,
            email = email,
            **kwargs
        )

        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        return user

    def create_superuser(self, full_name, email, password, **kwargs):
        user = self.create_user(
            full_name = full_name,
            email = email,
            password = password,
            **kwargs
        )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    full_name = models.CharField(verbose_name = "Nome Completo", max_length = 200, unique = True)
    email = models.EmailField(verbose_name = "E-mail", max_length = 194, unique = True) 
    is_staff = models.BooleanField(verbose_name = "Usuário desenvolvedor", default = False)
    is_superuser = models.BooleanField(verbose_name = "Super usuário", default = False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    objects = UserManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "users"
        app_label = "users"

    def get_short_name(self):
        # split_full_name = self.full_name.split()
        # return str(split_full_name[0] + " " + split_full_name[len(last_name_split) - 1])
        return self.full_name

    def get_full_name(self):
        return str(self.full_name)

    def get_absolute_url(self):
        return reverse('index')
        # return reverse('index', args=[str(self.id)]) CASO NECESSITASSE PASSAR ID

    def __str__(self):
        return self.get_full_name()
