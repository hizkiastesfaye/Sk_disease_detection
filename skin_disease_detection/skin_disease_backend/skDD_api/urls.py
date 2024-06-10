from django.urls import path
from .views import ProfileCreate, ProfileDetail, DataHistoryCreate, DataHistoryDetail

urlpatterns = [
    path('profile/',ProfileCreate.as_view(), name= 'profilecreate'),
    path('profile/<str:email>/',ProfileDetail.as_view(), name= 'profiledetail'),
    path('chat/', DataHistoryCreate.as_view(), name = 'datahistorycreate'),
    path('chat/<str:email>/', DataHistoryDetail.as_view(), name='datahistorydetail'),
    ]
