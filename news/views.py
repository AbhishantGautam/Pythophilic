from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="accounts")
def show_news(request):
    page = requests.get("https://www.infoworld.com/category/python/")
    soup = BeautifulSoup(page.content,"html.parser")
    link_list = soup.find_all(["div, class_='river-well'",'div, class_="post-cont"', "h3", "a"])
    dict_1={}
    for item in link_list[::2]:
        title = item.text
        locn = item.get("href")
        if locn and locn.startswith("/article" or "/video"):
            dict_1[title] = "https://www.infoworld.com" + str(locn)
    return render(request, "news/news.html", context={
        "dict_1" : dict_1
    })