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
            long_url = form.cleaned_data.get('long_url')
            if len(Urls.objects.filter(long_url=long_url) ) > 0:
           
                print(Urls.objects.filter(long_url=long_url)[0])
               
            else:
                print("saved")
                newUrl= Urls(long_url = long_url , short_url=index)
                newUrl.save()
    else:
            form = UrlForm()
    data = {'form': form}
    return render (request, 'pages/home.html',data)



def reroute(request, pk):
    if len(Urls.objects.filter(short_url=pk)) > 0:
        url = str(Urls.objects.filter(short_url=pk)[0])
        if url.startswith("http://"):
            return redirect(url)
        else:
            return redirect("http://"+url)
    else:
        return redirect('home')



# def newurl(request)
