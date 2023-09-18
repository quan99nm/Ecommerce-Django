from django.urls import path
from ecomerce.inventory.product.api.ProductApi import (
    ProductListView,
    ProductRetrieveView,
    CategoryListView,
    ProductsInCategoryView,
    product_image,
    NewestProductsView,
    CreateOrderView,
)

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductRetrieveView.as_view(), name="product-detail"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path(
        "categories/<int:category_id>/products/",
        ProductsInCategoryView.as_view(),
        name="products-in-category-list",
    ),
    path("products/<int:product_id>/image/", product_image, name="product_image"),
    path("products/newest/", NewestProductsView.as_view(), name="newest-product"),
    path("orders/create_order/", CreateOrderView.as_view(), name="create_order"),
]
