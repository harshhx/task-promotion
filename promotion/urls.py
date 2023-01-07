from django.urls import path, include
from .views import Welcome, CreatePlan
urlpatterns = [
    path('', Welcome.as_view()),
    path('create-plan/', CreatePlan.as_view())
]