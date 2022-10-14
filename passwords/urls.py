from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="password-home"),
    path("password/<int:password_id>/", views.password, name="password"),
    path("create/", views.create, name="create"),
    path("delete/<int:password_id>/", views.delete, name="delete")
]