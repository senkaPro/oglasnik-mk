from django.conf.urls import url

from . import views





app_name = 'profiles'

urlpatterns = [
    url(r'^$',views.BaseView.as_view(),name='base'),
    url(r'^register/$',views.RegisterView.as_view(),name='register'),
    url(r'^login/$',views.SignInView.as_view(),name='login'),
    url(r'^logout/$',views.SignOutView.as_view(),name='logout'),
    
]
