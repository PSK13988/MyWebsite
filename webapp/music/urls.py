from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.AlbumListView.as_view(), name='home'),
    # /youtube
    path('youtube/', views.redirect_to_youtube, name='redirect_to_youtube'),

    path('<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail')
]
