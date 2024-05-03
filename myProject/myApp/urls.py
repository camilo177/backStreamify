from .views import CreateInfoView
from .views import UpdateInfoView
from .views import ReadInfoView
from django.urls import path


urlpatterns = [
    path('createInfo', CreateInfoView.as_view()),
    path('updateInfo', UpdateInfoView.as_view()),
    path('readInfo', ReadInfoView.as_view()),
]