from rest_framework import serializers
from ecomerce.inventory.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")

    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "category_name", "image"]

    def create(self, validated_data):
        # Override the create method to add custom logic if needed
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Override the update method to update the product instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class ProductsInCategorySerializer(serializers.Serializer):
    categoryname = serializers.CharField(source="name")
    data = ProductSerializer(many=True)
