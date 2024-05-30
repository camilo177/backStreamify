from .views.create_info_view import CreateInfoView
from .views.update_info_view import UpdateInfoView
from .views.read_info_view import ReadInfoView
from .views.delete_info_view import DeleteInfoView
from .views.create_admin_profile_view import CreateAdminProfileView
from .views.update_info_view import GetInfoView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('createInfo', CreateInfoView.as_view()),
    path('updateInfo/id=<int:pk>', UpdateInfoView.as_view(), name='update_info'),
    path('readInfo', ReadInfoView.as_view(), name='read_info'),
    path('deleteInfo/id=<int:pk>', DeleteInfoView.as_view(), name='delete_info'),
    path('getInfo/<int:pk>', GetInfoView.as_view(), name='get_info'),
    path('createAdminProfile/', CreateAdminProfileView.as_view(), name='create_admin_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)