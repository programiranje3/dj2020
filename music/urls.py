"""URL Configs of the music app.
"""
from django.http import HttpResponse
from django.urls import path

from music import views

# urlpatterns = [
#     path('', views.index, name='index')
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]

urlpatterns += [
    path('bands/', views.BandListView.as_view(), name='band-list'),
    path('bands/<int:pk>/', views.BandDetailView.as_view(), name='band-detail'),
    path('bands/create/', views.BandCreateView.as_view(), name='band-create'),
    path('bands/update/<int:pk>/', views.BandUpdateView.as_view(), name='band-update'),
    path('bands/delete/<int:pk>/', views.BandDeleteView.as_view(), name='band-delete'),
]

urlpatterns += [
    path('musicians/', views.MusicianListView.as_view(), name='musician-list'),
    path('musicians/<int:pk>/', views.MusicianDetailView.as_view(), name='musician-detail'),
    path('musicians/create/', views.MusicianCreateView.as_view(), name='musician-create'),
    path('musicians/update/<int:pk>/', views.MusicianUpdateView.as_view(), name='musician-update'),
    path('musicians/delete/<int:pk>/', views.MusicianDeleteView.as_view(), name='musician-delete'),
]


