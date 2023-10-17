from django.urls import path

from back_app.views import user
from back_app.views import product
from back_app.views import checkout
from back_app.views import category
from back_app.views import filter
from back_app.views import price
from back_app.views import contenant_type
from back_app.views import brand

urlpatterns = [
    path("create-checkout-session/", checkout.CheckoutCollection.as_view()),
    path("category/", category.CategoryCollection.as_view()),
    path("brand/", brand.BrandCollection.as_view()),
    path("checkout-success/", checkout.CheckoutSuccess.as_view()),
    path("delete-order/<int:id>/", checkout.CheckoutCancel.as_view()),
    path("search/", filter.FilterCollection.as_view()),
    path("login/", user.UserCollection.as_view()),
    path("product/", product.ProductsCollection.as_view()),
    path("product/<int:id>/", product.ProductDetailsCollection.as_view()),
    path("inscription/", user.UserInscriptionCollection.as_view()),
    path("prices-min-max/", price.PriceCollection.as_view()),
    path("contenant-type/", contenant_type.ContenantTypeCollection.as_view()),
]
