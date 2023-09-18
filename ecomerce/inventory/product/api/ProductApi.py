from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ecomerce.inventory.models import Product, Category  # Import your Product model
from ecomerce.inventory.serializers.ProductSerializer import (
    ProductSerializer,
    CategorySerializer,
    ProductsInCategorySerializer,
    OrderSerializer,
)
from rest_framework import generics

from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# Import your Product serializer


# View for listing all products
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


# View for retrieving a single product
class ProductRetrieveView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsInCategoryView(generics.ListAPIView):
    serializer_class = ProductsInCategorySerializer

    def list(self, request, *args, **kwargs):
        category_id = self.kwargs.get("category_id")
        try:
            category = Category.objects.get(id=category_id)
            products = Product.objects.filter(category=category)
            serialized_products = ProductSerializer(
                products, many=True
            ).data  # Serialize products
            return Response(
                {"Category name": category.name, "data": serialized_products}
            )
        except Category.DoesNotExist:
            return Response({"detail": "Category not found."}, status=404)


def product_image(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.image:
        image_path = product.image.path
        with open(image_path, "rb") as image_file:
            return HttpResponse(
                image_file.read(), content_type="image/jpeg"
            )  # Adjust content_type if needed
    else:
        return HttpResponse(status=404)


class NewestProductsView(generics.ListAPIView):
    queryset = Product.objects.all().order_by("-id")[:3]  # Retrieve 3 newest products
    serializer_class = ProductSerializer


class CreateOrderView(APIView):
    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
