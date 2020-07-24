from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('music/', views.music_list),
    path('music/<int:pk>/', views.music_detail),

    path('class/music/', views.MusicList.as_view()),
    path('class/music/<int:pk>/', views.MusicDetail.as_view()),

    path('mixin/music/', views.MixinMusicList.as_view()),
    path('mixin/music/<int:pk>/', views.MixinMusicDetail.as_view()),

    path('generic/music/', views.GenericMusicList.as_view()),
    path('generic/music/<int:pk>/', views.GenericMusicDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)