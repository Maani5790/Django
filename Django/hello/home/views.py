        #   render use for templates


from multiprocessing import context
from urllib import response
from django.shortcuts import render, HttpResponse

# Create your views here.
def index (request):
    context = {
        'variable' : "im clever programmer",
        'variable2' : "im clever " 

    }
    return render(request , 'index.html')
    # return HttpResponse("this is homepage")



def about (request):
    return render(request , 'about.html' )
    # return HttpResponse("this is about page")

def services (request):
    return render(request , 'services.html')
    # return HttpResponse("this is services") 


def contact (request):
    # return HttpResponse("this is contact page")   
    return render(request , 'contact.html' )

