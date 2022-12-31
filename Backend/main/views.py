from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome My First Todo App</h1>')