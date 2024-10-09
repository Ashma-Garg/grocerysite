from django.http import HttpResponse 
from .models import Type, Item
from django.shortcuts import render, get_object_or_404
from django.views import View

def index(request):
     type_list = Type.objects.all().order_by('id') 
     response = HttpResponse() 
     heading1 = '<p>' + 'Different Types: ' + '</p>' 
     response.write(heading1)
     for type in type_list:
        para = '<p>'+ str(type.id) + ': ' + str(type) + '</p>' 
        response.write(para) 
     return response

def index1(request):
     item_list = Item.objects.all().order_by('-price')[:10]
     response = HttpResponse() 
     heading1 = '<p>' + 'Different Types: ' + '</p>' 
     response.write(heading1)
     for type in item_list:
        para = '<p>'+ str(type.name) + ': ' + str(type.price) + '</p>' 
        response.write(para) 
     return response


def about(request, year, month):
    # Dictionary to map month numbers to month names
    month_names = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December',
    }
    
    month_name = month_names.get(month, 'Invalid Month') 
    
    context = {
        'year': year,
        'month': month_name,  
    }
    return render(request, 'index.html', context)


def detail(request, type_no):
    # Use get_object_or_404 to fetch the item type or return a 404 if it doesn't exist
    item_type = get_object_or_404(Type, id=type_no)
    item_list = Item.objects.filter(type=item_type)
    
    response = HttpResponse()
    heading1 = '<p>' + 'Different Types: ' + '</p>' 
    response.write(heading1)
    
    for item in item_list:
        para = '<p>' + item.name + '</p>' 
        response.write(para)
    
    return response


# Function-Based View (FBV)
# Simple function handling request. 
# Can get cluttered when handling multiple HTTP methods.
def hello_fbv(request):
    return HttpResponse("Hello, this is a Function-Based View!")

# Class-Based View (CBV)
# Organized into a class with methods (get, post) to handle different HTTP requests.
# More scalable and reusable with inheritance and mixins.
class HelloCBV(View):
    def get(self, request):
        return HttpResponse("Hello, this is a Class-Based View!")
    

# Key Differences:
# - FBV is a function; CBV is a class with methods for different HTTP verbs.
# - CBVs allow for code reuse and cleaner handling of complex views.
# - FBV uses conditionals for HTTP methods, CBV uses separate methods like `get()` or `post()`.