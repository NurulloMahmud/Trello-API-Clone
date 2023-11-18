from django.urls import path
from projects.views import ProjectCreateAPIView, ProjectUpdateDeleteAPIView, ProjectRetrieveAPIView



urlpatterns = [
    path('projects-list/', ProjectRetrieveAPIView.as_view(), name='projects'),
    path('project/<int:pk>/', ProjectUpdateDeleteAPIView.as_view(), name='update-delete-project'),
    path('project-create/', ProjectCreateAPIView.as_view(), name='project-create'),
]