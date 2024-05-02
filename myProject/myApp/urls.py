from .views import NominaView
from django.urls import path


urlpatterns = [
    path('nomina', NominaView.as_view()),
]