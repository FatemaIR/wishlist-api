from rest_framework import serializers
from items.models import Item, FavoriteItem
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'first_name', 'last_name']


class UserCreateSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['first_name', 'last_name']

class ItemListSerializer(serializers.ModelSerializer):
	added_by = UserSerializer()
	num_of_users = serializers.SerializerMethodField()
	detail = serializers.HyperlinkedIdentityField(
		view_name = "api-detail",
		lookup_field = "id",
		lookup_url_kwarg = "item_id"
		)
	def get_num_of_users(self, obj):
		num_users = FavoriteItem.objects.filter(item=obj)
		return num_users.count()

	class Meta:
		model = Item
		fields = ['name', 'description', 'detail', 'added_by','num_of_users']

class ItemDetailSerializer(serializers.ModelSerializer):
	all_users = serializers.SerializerMethodField()

	class Meta:
		model = Item
		fields = ['image', 'name', 'description', 'added_by', 'all_users']

	def get_all_users(self, obj):
		all_users = FavoriteItem.objects.filter(item=obj)
		return UserSerializer(all_users, many=True).data        

