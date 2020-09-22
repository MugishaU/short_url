from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    form = UrlForm()
    # index = Urls.objects.all().length()

    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            newUrl= Urls(long_url = form.cleaned_data.get('long_url'), short_url=f'shorturl/{1+1}')
            newUrl.save()
    else:
            form = UrlForm()
    data = {'form': form}
    return render (request, 'pages/home.html',data)
