from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Account Routes for Adventure Buddy
urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('edit_info/', views.edit_info, name='edit_info'),
  # WORKING HERE
  # path('update_profile', views.update_profile, name='update_profile'),
  path('change_password', views.change_password, name='change_password'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
