from django.shortcuts import render

# Create your views here.


def home(request):
    name = 'sawacha'
    return render(request, 'accounts/home.html')

