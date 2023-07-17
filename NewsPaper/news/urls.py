from django.urls import path
from .views import PostsList, PostView, PostCreate, PostUpdate, PostDelete, PostSearch, CategoryListView, subscribe

urlpatterns = [
   path('', PostsList.as_view(), name='news'),
   path('<int:pk>', PostView.as_view(), name='post_detail'),
   path('create/', (PostCreate.as_view()), name='post_create'),
   path('article/create/', PostCreate.as_view(), name='article_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='product_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('search', PostSearch.as_view(), name='search'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe')
]