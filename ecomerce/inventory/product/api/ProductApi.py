from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ecomerce.inventory.models import Product, Category  # Import your Product model
from ecomerce.inventory.serializers.ProductSerializer import (
    ProductSerializer,
    CategorySerializer,
    ProductsInCategorySerializer,
)
from rest_framework import generics

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
