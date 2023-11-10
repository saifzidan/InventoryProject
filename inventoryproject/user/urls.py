from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name = "user"
urlpatterns = [
    path("register/", user_views.register, name="register"),
    path("profile/", user_views.profile, name="profile"),
    path("profile/update/", user_views.profile_update, name="profile-update"),
    path(
        "", auth_views.LoginView.as_view(template_name="user/login.html"), name="login"
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="user/logout.html"),
        name="logout",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
