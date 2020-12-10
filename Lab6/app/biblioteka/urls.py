from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import  KsiazkaList
from .views import UserViewSet

# from .views import UserList, UserDetail, PostList, PostDetail
#from .views import UserViewSet, PostViewSet


# urlpatterns = [
    # path('users/', UserList.as_view()),
    # path('users/<int:pk>/', UserDetail.as_view()), 

    # path('<int:pk>/', KsiazkaDetail.as_view()),
    # path('', KsiazkaList.as_view()),
# ]

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', KsiazkaList, basename='Ksiazki')
urlpatterns = router.urls
