# posts urls.py
# TODO convert url regex to path
from django.conf.urls import url

from . import views

app_name = 'posts'

urlpatterns = [
    url(r"^$", views.PostList.as_view(), name="all"),
    url(r"new/$", views.CreatePost.as_view(), name="create"),
    url(r"by/(?P<username>[-\w]+)/$",
        views.UserPosts.as_view(), name="for_user"),
    url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",
        views.PostDetail.as_view(), name="single"),
    url(r"delete/(?P<pk>\d+)/$", views.DeletePost.as_view(), name="delete"),
]


###PATH IMPLEMENTATION###
#from django.urls import path
#from . import views

# app_name = 'posts'  # allows us to use this in our template tags

# urlpatterns = [
#path('', views.PostList.as_view(), name='all'),
#path('new/', views.CreatePost.as_view(), name='create'),
#path('by/<int:username>/', views.UserPosts.as_view(), name='for_user'),
#path('by/<int:username>/', views.PostDetail.as_view(), name='single'),
#path('delete/<int:pk>/', views.DeletePost.as_view(), name='delete')
#]
