from django.http import HttpResponse
from django.shortcuts import render


def home(request):
   # return HttpResponse("Hello Sumit")
     return render(request, 'website/index.html')


def about(request):
    return HttpResponse("Tell me about yourself")


def contact(resquest):
    return HttpResponse("Give your contact detail")