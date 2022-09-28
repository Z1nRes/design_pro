from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('myapplications', views.LoanedApplicationsByUserListView.as_view(), name='my-applications'),
    re_path(r'^application/(?P<pk>\d+)$', views.ApplicationDetailView.as_view(), name='application-detail'),
    re_path(r'^application/create/$', views.ApplicationCreate.as_view(), name='create'),
    re_path(r'^application/(?P<pk>\d+)/delete/$', views.ApplicationDelete.as_view(), name='delete'),
]
