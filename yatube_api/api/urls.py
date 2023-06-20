from django.urls import include, path
from rest_framework.routers import DefaultRouter

import api.views as views

router_v1 = DefaultRouter()

router_v1.register('posts', views.PostViewSet, basename='posts')
router_v1.register('groups', views.GroupViewSet, basename='group')
router_v1.register('follow', views.FollowViewSet, basename='follow')
router_v1.register(
    r'^posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
