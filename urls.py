from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListSyoukaiView.as_view(),name='index'),
    path('link/',views.LinkSyoukaiView.as_view(),name='link'),
    path('about/',views.AboutSyoukaiView.as_view(),name='about'),
    path('gallery/',views.GallerySyoukaiView.as_view(),name='gallery'),
    path('comment/', views.CommentSyoukaiView.as_view(), name='comment'),
]
