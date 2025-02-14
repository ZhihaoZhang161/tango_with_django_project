from django.shortcuts import render

from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):

     #Query the database for a list of ALL categories currently stored.
    #Order the categories by no. likes in descending order.
    #Retrieve the top 5 only - or all if less than 5.
    #Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

   
    context_dict = {}
    context_dict['boldmessage']= 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')


def show_category(request, category_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context_dict)

# Create your views here.
