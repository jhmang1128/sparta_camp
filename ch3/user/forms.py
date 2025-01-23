from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class UserChangeForm_custom(UserChangeForm):
    class Meta:
        password = None
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "email",
            "introduce",
        ]
        
        
class UserCreationForm_custom(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ()
        