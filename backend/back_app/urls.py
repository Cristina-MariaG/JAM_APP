from django.urls import path

from back_app.views import views
from back_app.views import user
from back_app.views import product
from back_app.views import checkout
from back_app.views import category
from back_app.views import filter

urlpatterns = [
    path("", views.Collection.as_view()),
    path("create-checkout-session/", checkout.CheckoutCollection.as_view()),
    path("category/", category.CategoryCollection.as_view()),
    path("checkout-success/", checkout.CheckoutSuccess.as_view()),
    path("filter/", filter.FilterCollection.as_view()),
    path("login/", user.UserCollection.as_view()),
    path("product/", product.ProductsCollection.as_view()),
    path("product/<int:id>/", product.ProductDetailsCollection.as_view()),
    path("signup/", user.UserSignupCollection.as_view()),
]
