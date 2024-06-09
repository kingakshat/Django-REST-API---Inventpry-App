"""inventoryproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from inventortapp.views import test, InventoryView, Item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test.as_view(), name = 'test'),
    path('items/<str:resource>/', Item.as_view(), name='Item-sort-resource'),
    path('items/<str:resource>/<str:category>/', Item.as_view(), name='Item-query-resource'),
    path('inventory/<str:resource>/', InventoryView.as_view(), name='Inventory-read-write'),
    path('inventory/<str:resource>/<int:item_id>/', InventoryView.as_view(), name='Inventory-update'),
]
