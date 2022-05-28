from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('settings/', views.settings, name="settings"),
    path('<str:username>/', views.public_profile, name="public_profile"),
    path('<str:username>/follow', views.follow, name="follow"),
    path('<str:username>/unfollow', views.unfollow, name="unfollow"),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)