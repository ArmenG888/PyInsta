from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.welcome_page, name="welcome-page"),
    path('h/', views.home, name="home"),
    path('explore/', views.explore, name="explore"),
    path('p/<id>', views.post_detail_view, name="post-detail"),
    path('p/<id>/delete/', views.delete_post, name="delete"),
    path('<id>/like/', views.like, name="post-like"),
    path('p/<id>/delete/', views.delete_post, name="delete"),
    path('p/<id>/like/', views.like_detail, name="post-like-detail"),
    path('p/<id>/<comment_id>/like', views.comment_like, name="comment-like"),
    path('p/<post_id>/<comment_id>/', views.comment_detail, name="comment-detail"),
    path('search/', views.home, name="user-search"),
    path('p/new_post/', views.new_post, name="new-post"),
    path('ajax/', views.live_data, name="live_data"),
    path('ajax/<post_id>', views.live_like_data, name="live_like_data")

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)