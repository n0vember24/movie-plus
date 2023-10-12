from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserListView(ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = AllowAny,


class UserRetrieveView(RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = AllowAny,
