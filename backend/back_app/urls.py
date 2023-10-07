from django.urls import path

from back_app.views import views
from back_app.views import user

urlpatterns = [
    path("", views.Collection.as_view()),
    path("login/", user.UserCollection.as_view()),
    path("signIn/", user.UserSignInCollection.as_view()),
]
