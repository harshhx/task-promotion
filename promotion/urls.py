from django.urls import path, include
from .views import Welcome, CreatePlan, CreatePromotion
urlpatterns = [
    path('', Welcome.as_view()),
    path('create-plan/', CreatePlan.as_view()),
    path('create-promotion/', CreatePromotion.as_view())
]