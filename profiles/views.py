from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView,LoginView
from django.contrib.auth import login,authenticate
from django.conf import settings
from django.http import Http404
from django.shortcuts import render,HttpResponseRedirect,reverse,get_object_or_404
from django.views.generic import TemplateView,FormView,DetailView,UpdateView,ListView
from .forms import RegisterForm,AuthenticationForm,ProfileForm
from .models import Profile

User = get_user_model()

class BaseView(TemplateView):
    template_name = 'profiles/base.html'

    def get(self,request,*args,**kwargs):
        template_name = 'profiles/base.html'
        qs = User.objects.all().order_by('-date_joined')[:5]
        return render(request,template_name,{'users':qs})


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'profiles/register.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return HttpResponseRedirect(reverse('profiles:base'))

class SignOutView(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL
    template_name = 'profiles/base.html'


class SignInView(LoginView):
    template_name = 'profiles/login.html'
    redirect_field_name = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        user = form.get_user()
        login(self.request, user)
        return HttpResponseRedirect(reverse(settings.LOGIN_REDIRECT_URL),{'user':user})
