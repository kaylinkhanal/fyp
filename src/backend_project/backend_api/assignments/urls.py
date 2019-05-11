from rest_framework.routers import DefaultRouter
from backend_api.views import AssignmentViewSet

router = DefaultRouter()
router.register(r'', AssignmentViewSet, base_name='assignments')
urlpatterns = router.urls
