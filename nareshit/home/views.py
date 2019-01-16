from django.http import HttpResponse

def index(request):
    return HttpResponse("<html><body bgcolor='#FFC300'><h1>Welcome to Django World</h1></body></html>")
