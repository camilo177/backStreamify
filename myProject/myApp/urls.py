from myApp.views import CreateInfoView
from myApp.views import UpdateInfoView
from myApp.views import ReadInfoView
from myApp.views import DeleteInfoView
from myApp.views import CreateAdminProfileView
from myApp.views import WatchProductionView
from django.urls import path


urlpatterns = [
    path('createInfo', CreateInfoView.as_view()),
    path('updateInfo', UpdateInfoView.as_view()),
    path('readInfo', ReadInfoView.as_view()),
    path('deleteInfo/<int:pk>', DeleteInfoView.as_view()),
    path('createAdminProfile', CreateAdminProfileView.as_view()),
    path('watchProduction', WatchProductionView.as_view())
]