from django.contrib import admin
from .models import register, Report, Solution

admin.site.register(Solution)
admin.site.register(Report)
admin.site.register(register)
