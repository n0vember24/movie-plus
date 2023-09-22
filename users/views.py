from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # TODO
    # def get_queryset(self, request):
    # 	if request.action == 'GET':
    # 		self.permission_classes = IsAdmin
    # 	return self.get_queryset()
