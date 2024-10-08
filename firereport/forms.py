from django.contrib.auth.forms import UserCreationForm # type: ignore
from . models import *
class RegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email',  'password1', 'password2']