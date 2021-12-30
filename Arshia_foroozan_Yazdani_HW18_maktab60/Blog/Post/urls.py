from django.urls import path
from .views import CommentApiView, CommentApiVDetail, PostApiView, PostApiDetail, CommentPostApiView

urlpatterns = [
    path('comments/', CommentApiView.as_view()),
    path('posts/', PostApiView.as_view()),
    path('posts/<int:pk>', PostApiDetail.as_view()),
    path('comments/<int:pk>', CommentApiVDetail.as_view()),
    path('commentpost/<int:pk>', CommentPostApiView.as_view()),

]