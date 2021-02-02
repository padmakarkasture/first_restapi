from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

...

schema_view = get_schema_view(
   openapi.Info(
      title="profile api",
      default_version='v1',
      description="made with viewsets",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="kasturepadmakar4u@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router=SimpleRouter()
router.register('api', views.profile_viewset)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
  

]
