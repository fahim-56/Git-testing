from django.http import HttpResponse

def contact (request):
    return HttpResponse("Contact Page")

def home (request):
    return HttpResponse("Home Page of firstProject")

def fahim (request):
    return HttpResponse("Fahim's Page")