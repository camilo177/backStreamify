from .views.watch_view import WatchProductionView
from .views.create_info_view import CreateInfoView
from .views.update_info_view import UpdateInfoView
from .views.read_info_view import ReadInfoView
from .views.delete_view import DeleteInfoView
from .views.create_admin_profile_view import CreateAdminProfileView
from .views.create_view import CreateProductionView

from django.urls import path

urlpatterns = [
    path('createInfo', CreateInfoView.as_view()),
    path('updateInfo/id=<int:pk>', UpdateInfoView.as_view(), name='update_info'),
    path('readInfo/id=<int:pk>', ReadInfoView.as_view(), name='read_info'),
    path('deleteInfo/id=<int:pk>', DeleteInfoView.as_view(), name='delete_info'),
    path('createAdminProfile', CreateAdminProfileView.as_view()),
    path('createProduction', CreateProductionView.as_view()),
    path('watchProduction/id=<int:pk>', WatchProductionView.as_view(), name='watch_production')
]