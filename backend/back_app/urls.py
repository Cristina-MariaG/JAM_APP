from django.urls import path

from back_app.views import views
from back_app.views import user
from back_app.views import product

urlpatterns = [
    path("", views.Collection.as_view()),
    path("login/", user.UserCollection.as_view()),
    path("signup/", user.UserSignupCollection.as_view()),
    path("product/", product.ProductsCollection.as_view()),
    path("product/<int:id>/", product.ProductDetailsCollection.as_view()),
]
