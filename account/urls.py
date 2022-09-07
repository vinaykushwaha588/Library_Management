
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

## Creating An Object DefaultRouter() --
router = DefaultRouter()

## Register Here DefaultRouter Objects
router.register('book',BookList,basename='modelviewset')


## BASE_URl = http//127.0.0.1:8000/account/

urlpatterns = [
    path("send-otp/", SignUpUser.as_view()),
    path("verify/", verifyOTPView.as_view()),
    path('login/',LoginUser.as_view()),
    path("list/", include(router.urls)),

]

