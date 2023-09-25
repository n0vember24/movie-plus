from rest_framework.generics import ListAPIView, RetrieveAPIView
from users.models import User
from users.serializers import UserSerializer


class UserListRetrieveView(ListAPIView, RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
