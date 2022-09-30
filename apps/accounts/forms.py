from django import forms
from accounts.models import User

class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(
        max_length = 60, 
        required = True, 
        label = "Confirmação de Senha",
        error_messages = {
            "required": "A confirmação de senha é obrigatória para realizar o registro!",
            "invalid": "Por favor, insira uma confirmação de senha válida!",
        },
    )

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit = False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user

    class Meta:
        model = User

        fields = ["full_name", "email", "password", "confirm_password" ]

        error_messages = {
            "full_name":{
                "required": "O nome é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um nome válido!",
            },
            "email":{
                "required": "O e-mail é obrigatório para realizar o registro!",
                "invalid": "Por favor, insira um e-mail válido!",
            },
            "password":{
                "required": "A senha é obrigatória para realizar o registro!",
                "invalid": "Por favor, insira uma senha válida!",
            },
        }
