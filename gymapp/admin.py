# Registering the models created in models.py
from django.contrib import admin
from .models import Plan, Trainer, Member

admin.site.register(Plan)
admin.site.register(Trainer)
admin.site.register(Member)


