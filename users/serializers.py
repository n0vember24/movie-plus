from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
	class Meta:
		model = User
		exclude = (
			'password', 'is_staff', 'is_active',
			'date_joined', 'last_login'
		)
