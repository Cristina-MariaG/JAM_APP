from django.urls import path

from back_app.views import views
from back_app.views import user

urlpatterns = [
    path("", views.Collection.as_view()),
    path("user/", user.UserCollection.as_view()),
]
