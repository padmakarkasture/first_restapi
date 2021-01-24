from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Rest api by Padmakar",
      default_version='v1',
      description="first api ever i made and deployed for test",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kasturepadmakar4u@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router=SimpleRouter()
router.register(r'', views.profile_viewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
