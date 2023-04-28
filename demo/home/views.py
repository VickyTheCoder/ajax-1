from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
# Create your views here.
def homepage(req):
    return render(req, 'index.html')

def current_time(req):
    n = datetime.now()
    return JsonResponse({'time': str(n)})
