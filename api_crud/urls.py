
from django.contrib import admin
from django.conf.urls import include, url
from .views import RegisterView, CustomLoginView


from fcm_django.api.rest_framework import FCMDeviceViewSet, FCMDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register(r'devices', FCMDeviceViewSet)

# urls
urlpatterns = [
    url(r'^movies/', include('movies.urls')),
    url(r'^docs/', include_docs_urls(title='FCM django web demo')),
    url(r'^fcm/', include(router.urls)),
    url(r'^rest-auth/login/', CustomLoginView.as_view()),
    url(r'^rest-auth/registration/', RegisterView.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^admin/', admin.site.urls),
]