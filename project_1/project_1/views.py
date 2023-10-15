from django.http import HttpResponse


def home(request):
    return HttpResponse("This is home page")
def contact(request):
    return HttpResponse("This is contact page")