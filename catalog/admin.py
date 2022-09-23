from django.contrib import admin
from .models import User, Category, Application

admin.site.register(User)
admin.site.register(Application)
admin.site.register(Category)
