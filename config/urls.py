from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg.openapi import Contact, Info, License
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

API_DESCRIPTION = """
The API for the project called "Movie Plus" is designed to provide an enjoyable movie 
viewing experience without worrying about time being wasted.
"""

schema_view = get_schema_view(
	Info(
		"Movie Plus API", 'v1', API_DESCRIPTION, "https://www.google.com/policies/terms/",
		Contact('Telegram', 'htts://t.me/n0vember24'), License(name="MIT License"),
	),
	public=True,
	permission_classes=[AllowAny]
)

urlpatterns = [
	path('api/', include('movies.urls')),
	path('api/users/', include('users.urls')),
	path('admin/', admin.site.urls),
	# Swagger
	path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	path('<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
	path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
