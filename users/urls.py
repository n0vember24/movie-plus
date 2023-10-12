from django.urls import path

from users.views import UserListView, UserRetrieveView

# router = DefaultRouter()
# router.register('users', UserViewSet)
# urlpatterns = router.urls

urlpatterns = [
	path("users", UserListView.as_view(), name="user-list-view"),
	path("users/<int:pk>/", UserRetrieveView.as_view(), name="user-retrieve-view"),
]
