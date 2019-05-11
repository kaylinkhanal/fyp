from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('assignments/', include('backend_api.assignments.urls')),
    path('graded-assignments/', include('backend_api.graded_assignments.urls')),
    path('users/', include('backend_api.urls')),
    re_path(r'index/', TemplateView.as_view(template_name='index.html')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,})
]
