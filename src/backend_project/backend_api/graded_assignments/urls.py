from django.urls import path
from backend_api.views import GradedAssignmentListView, GradedAssignmentCreateView

urlpatterns = [
    path('', GradedAssignmentListView.as_view()),
    path('create/', GradedAssignmentCreateView.as_view()),
]
