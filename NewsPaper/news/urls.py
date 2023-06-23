from django.urls import path
from .views import PostsList, PostView


urlpatterns = [
   path('', PostsList.as_view()),
   path('<int:pk>', PostView.as_view(), name='post_detail'),
]