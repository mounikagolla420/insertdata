from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('insert the topic is successfully')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('webpage data is submitted')
    return render(request,'insert_webpage.html')


def insert_accessrecords(request):
    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']
        WO=Webpage.objects.get_or_create(name=name)[0]
        WO.save()
        AO=AccessRecords.objects.get_or_create(name=WO,author=author,date=date)[0]
        AO.save()
        return HttpResponse('accessrecords insertion is done Successfully')

    return render(request,'insert_accessrecords.html')