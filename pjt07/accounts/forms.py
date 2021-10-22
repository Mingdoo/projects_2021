from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

user = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = user
        fields = UserCreationForm.Meta.fields


# class CustomUserChangeForm()