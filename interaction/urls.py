from django.urls import path, include
from . import views
from .api_views import LikeViewSet,BookmarkViewSet,CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("likes", LikeViewSet, basename="likes") 
router.register("bookmarks", BookmarkViewSet, basename="bookmarks") 
router.register("comments", CommentViewSet, basename="comments") 

app_name ="interaction"

urlpatterns = [
    path("viewsets/", include(router.urls)), # /todo/viewsets/view/

]
