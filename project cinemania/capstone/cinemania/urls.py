from django.urls import path
from .views import welcome, index, upload, home, User_login, Logout_user
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
	path('', welcome, name="welcome"),
	path('index', index, name="index"),
	path('upload/', upload, name="upload"),
	path('login/',User_login, name="loginuser"),
	path('home/', home, name="home"),
	path('logout/', Logout_user, name="logout")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)