from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests

# Create your views here.
API_KEY = 'eb03efec3932478c854c36f9cd5a4ddf'

def index(request):
    #return HttpResponse("Hello World")
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    # url = f'https://newsapi.org/v2/top-headlines/sources?apiKey={API_KEY}'
    # url = f'https://newsapi.org/v2/top-headlines/sources?country&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    article=data['articles']
   
    context={
        'article':article
    }
    return render(request,'index.html',context)
