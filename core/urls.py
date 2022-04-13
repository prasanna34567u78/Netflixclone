

from django.urls import  path
from .views import ProfileCreate,ProflieList,home,Watch,ShowMovieDetail,ShowMovie

app_name='core'

urlpatterns =[

    path('',home.as_view(),name='home'),
    path('profile/',ProflieList.as_view(),name='profile_list'),
    path('profile/create/',ProfileCreate.as_view(),name='profile_create'),
    path('watch/<str:profile_id>/',Watch.as_view(),name='watch'),
    path('movie/detail/<str:movie_id>/',ShowMovieDetail.as_view(),name='show_det'),
    path('movie/play/<str:movie_id>/',ShowMovie.as_view(),name='play')
]