from django.shortcuts import render

from topics.models import Topics
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="accounts")
def show_topics(request):
    topics = Topics.objects.all()
    shortlisted_topics = topics[6:12]
    context = {
        "topics" : topics,
        "dopics" : shortlisted_topics
    }
    return render(request,"topics/topics.html", context)

def show_details(request, slug_):
    topic = Topics.objects.get(slug = slug_)
    return render(request, "topics/detail.html",{
        "topic" : topic
    })