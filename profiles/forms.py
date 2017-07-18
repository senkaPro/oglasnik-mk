from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Profile
User = get_user_model()

class RegisterForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput, required=True)


    class Meta(UserCreationForm.Meta):

        model = User
        fields = ('email','password1','password2',)


    def save(self, commit=False):
        user = User.objects.create_user(
                                        self.cleaned_data.get('email'),
                                        self.cleaned_data.get('password1')
                                        )
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):

    def clean(self):
        return super(LoginForm,self).clean()

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        
