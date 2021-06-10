from django.urls import path
from . import views
from .views import PostListView, PostDetailView, buy

import users.views as user_views

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='product-home'),  # class based view
    # path('register/', user_views.register, name='register')
    path('product/<int:pk>/', PostDetailView.as_view(), name='product-detail'),
    path('buy/<int:pk>/', buy, name='buy-page'),

]
