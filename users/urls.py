from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import UserListRetrieveView

# router = DefaultRouter()
# router.register('users', UserViewSet)
# urlpatterns = router.urls

urlpatterns = [
    path("users", UserListRetrieveView.as_view(), name="user-list-view"),
    path("users/<int:pk>/", UserListRetrieveView.as_view(), name="user-retrieve-view"),
]
