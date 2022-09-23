from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    re_path(r'^myapplications$', views.LoanedApplicationsByUserListView.as_view(), name='my-applications'),
]
