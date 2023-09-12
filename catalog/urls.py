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

    path('admin-panel', views.adminPanel, name='admin_panel'),
    re_path(r'^application/(?P<pk>\d+)/update$', views.updateAdmin, name='update-admin'),

    path('admin-panel-category', views.adminPanelCategory, name='admin_panel_category'),
    re_path(r'^category/(?P<pk>\d+)/update$', views.updateAdminCategory, name='update-admin-category'),
    re_path(r'^category/create/$', views.CreateCategory.as_view(), name='create-category'),
    re_path(r'^category/(?P<pk>\d+)/delete/$', views.adminPanelCategoryDelete.as_view(), name='delete-category'),
]
