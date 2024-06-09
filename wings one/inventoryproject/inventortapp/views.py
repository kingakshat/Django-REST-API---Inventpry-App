from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import InventorySerializer


from .models import Inventory

# Create your views here.
class test(APIView):
    def get(self, request):
        text = 'w,khdbcuefcurhfbvjebfgv '
        return Response(text, content_type='text/html')

class InventoryView(APIView):
    def get(self, request, resource=None, item_id=None):
        if resource == 'items' and request.method == 'GET':
            items = Inventory.objects.all()
            serializer = InventorySerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, resource=None, item_id=None):
        if resource == 'items' and request.method == 'POST':
            serializer = InventorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else: 
                errors = serializer.errors
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
            
        
    def put(self, request, resource=None, item_id=None):
        if resource == 'items' and request.method == 'PUT' and item_id:
            try:
                item = Inventory.objects.get(id=item_id)
            except Inventory.DoesNotExist:
                return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = InventorySerializer(item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                errors = serializer.errors
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Invalid resource or item ID"}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, resource=None, item_id=None):
        if resource == 'items' and request.method == 'DELETE' and item_id:
            try:
                item = Inventory.objects.get(id=item_id)
                item.delete()
                return Response({"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
            except Inventory.DoesNotExist:
                return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Item ID is required"}, status=status.HTTP_400_BAD_REQUEST)
    
class Item(APIView):
    def get(self, request, resource=None, category=None):
        if resource == 'query' and request.method == 'GET' and category:
            items = Inventory.objects.filter(category=category)
            serializer = InventorySerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if resource == 'sort' and request.method == 'GET':
            items = Inventory.objects.all().order_by('-price')

            serializer = InventorySerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        