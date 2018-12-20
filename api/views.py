from django.shortcuts import render
from rest_framework.generics import (ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView, )
from items.models import Item, FavoriteItem
from .serializers import ItemListSerializer, ItemDetailSerializer, UserSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsAddedBy


class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description',]
    permission_classes = [AllowAny]
    


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [IsAuthenticated, IsAddedBy]





