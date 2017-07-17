from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from .forms import RegisterForm

class BaseView(TemplateView):
    template_name = 'profiles/base.html'


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'profiles/register.html'
    success_url = '/'

    def form_valid(self,form):
        form.save()
        return super(RegisterView,self).form_valid(form)
