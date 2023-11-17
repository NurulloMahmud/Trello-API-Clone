from django.urls import path
from . import views as v 




urlpatterns = [
    path('projects/', v.ProjectRetrieveAPIView.as_view(), name='projects'),
    path('project/<int:pk>/', v.ProjectUpdateDeleteAPIView.as_view(), name='update-delete-project'),
    path('project-create/', v.ProjectCreateAPIView.as_view(), name='project-create'),
]