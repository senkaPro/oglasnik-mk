from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class RegisterForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput, required=True)


    class Meta:
        UserModel = get_user_model()
        model = UserModel
        fields = ('email','password1','password2',)
        field_classes = {'email': forms.EmailField }

    def save(self, commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
