from django.urls import path
from . import views

urlpatterns = [
    path('person/<int:pk>/basicinfo/', views.getUserInfo, name='userinfo'),
    path('person/<int:pk>/collection/',views.getCollection, name='collection'),
    path('person/<int:pk>/towatch/',
         views.getTowatch, name='towatch'),

    path('movie/<str:pk>/info/', views.getMovieinfo,name='movieinfo'),
    # path('movie/recommend/regular/', ),
    # path('movie/recommend/specific_uesr/:uesrId', ),
]
