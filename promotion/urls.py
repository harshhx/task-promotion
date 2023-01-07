from django.urls import path, include
from .views import Welcome
urlpatterns = [
    path('', Welcome.as_view()),
]