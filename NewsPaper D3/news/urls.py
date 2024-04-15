from django.urls import path
from .views import PostList, PostDetail, Search, NewsCreate, \
    ArticleCreate, NewsEdit, ArticleEdit, NewsDelete, ArticleDelete, subscriptions, Index
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),  # cache_page(60)(PostList.as_view())
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),  # cache_page(300)(PostDetail.as_view())
    path('search/', Search.as_view(), name='search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('article/<int:pk>/edit/', ArticleEdit.as_view(), name='article_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('hello/', Index.as_view(), name='hello'),
]
