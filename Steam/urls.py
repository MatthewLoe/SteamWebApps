from django.urls import path
from . import views, WishlistScrape

app_name = 'Steam'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]

WishlistScrape.wishlistScrape()