from django.shortcuts import render
import datetime
# Create your views here.
def built_in_filters(request):
    data='hAi HEllo How aRe YOU'
    dt=datetime.datetime.now()
    d={'data':data,'dt':dt}
    return render(request,'built_in_filters.html',d)

def customfilters(request):
    data='helohelelo'
    d={'data':data}
    return render(request,'customfilters.html',d)