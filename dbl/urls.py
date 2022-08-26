from django.urls import include, path
from rest_framework import routers, permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from dbl.app import views
from dbl import settings 
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

schema_view = get_schema_view(
   openapi.Info(
      title="Inspectorio Test",
      default_version='v1',
      description="Test description"
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include(router.urls)),
    path(
        "api/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)