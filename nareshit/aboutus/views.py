from django.http import HttpResponse

def index(request):
    return HttpResponse("<html><body bgcolor='#6699ff'><h1>This is a About Us Page</h1></body></html>")
