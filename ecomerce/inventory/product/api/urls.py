from django.urls import path
from ecomerce.inventory.product.api.ProductApi import (
    ProductListView,
    ProductRetrieveView,
    CategoryListView,
    ProductsInCategoryView,
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
]
