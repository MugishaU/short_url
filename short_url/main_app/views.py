from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    form = UrlForm()
    index = 0
    # index='hey'

    for item in Urls.objects.all():
        index += 1

    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            print(index)
            newUrl= Urls(long_url = form.cleaned_data.get('long_url'), short_url=f'shorturl/{index}')
            newUrl.save()
    else:
            form = UrlForm()
    data = {'form': form}
    return render (request, 'pages/home.html',data)
