from .WishlistScraper.ProcessDiscounted import processData
from .WishlistScraper.ScrapeWishlist import get_wishlist
from .models import Game

"""
Author: Matthew Loe
Date Last Modified: 6/7/2020
Description: Script for running scrape
"""

def wishlistScrape():
    Game.objects.all().delete()

    #Edit url, replacing USERNAME with the user wishlist to be scraped  
    url = 'https://store.steampowered.com/wishlist/id/USERNAME/#sort=order'

    data = get_wishlist(url)
    data = processData(data)

    for x in data:
        create_game(x)

def create_game(game):
    Game.objects.create(name=game['name'], id=game['appid'], discount=game['discount'], 
                        original_price=game['original_price'], 
                        discount_price=['discount_price'])
