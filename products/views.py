from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from products.forms import IndexForm
from .models import Product


# Create your views here.



def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('yo')


def postit(request):
    inp = request.POST["innn"]
    inp1 = request.POST["innm"]
    products = Product.objects.all()





    return render(request, "chech.html",{'products': products,'inp':inp,'inp1':inp1})
