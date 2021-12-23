from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("This is a new homepage")
    # context = {
    #     "variable":"This is variable generated dynamically"
    # }
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("This is an about page")
    return render(request, 'about.html')
def services(request):
    # return HttpResponse("This is a services page")
    return render(request, 'services.html')
def contact(request):
    # return HttpResponse("This is a contact page")
    return render(request, 'contact.html')