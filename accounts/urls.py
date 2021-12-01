from django.urls import path
from . import views
urlpatterns = [
    path("", views.show_accounts, name="accounts"),
    path("register/", views.show_register, name="register"),
    path("token/", views.token_send, name="token"),
    path("success/", views.show_success, name="success"),
    path("verify/<auth_token>", views.show_verify, name="verify"),
    path("logout/", views.show_logout, name="logout")    
]