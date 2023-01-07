from django.contrib import admin
from .models import Plan, Promotion, CustomerGoal
# Register your models here.

admin.site.register(Plan)
admin.site.register(Promotion)
admin.site.register(CustomerGoal)
