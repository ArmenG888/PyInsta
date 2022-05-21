from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('direct/messages/', views.threads, name="threads"),
    path('<username>/chat/', views.new_chat, name="new_chat"),
    path('direct/messages/<id>', views.direct_messages, name="direct-messages"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)