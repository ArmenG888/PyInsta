from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name="home"),
    path('p/<id>', views.post_detail_view, name="post-detail"),
    path('<id>/like/', views.like, name="post-like"),
    path('p/<id>/like/', views.like_detail, name="post-like-detail"),
    path('p/<id>/<comment_id>/like', views.comment_like, name="comment-like"),
    path('search/', views.home, name="user-search")

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)