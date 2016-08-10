from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category


# Create your views here.

# Old simple index view
#def index(request):
#    return HttpResponse("""Rango says hey there world! 
#        <br/>See the <a href='/rango/about'>About</a> page.""")

#def about(request):
#    return HttpResponse("""Rango says here is the about page.
#        <br/> To go back to the index page 
#        click <a href='/rango/'>here</a>.""")

# New index view using template
# Now old -- new index shows category list (below)
# def index(request):
# 
#     # Construct a dictionary to pass to the template engine as its context.
#     # Note the key boldmessage is the same as {{ boldmessage }} in the template!
#     context_dict = {'boldmessage': "This is the text to be added to the template."}
# 
#     # Return a rendered response to send to the client.
#     # We make use of the shortcut function to make our lives easier.
#     # Note that the first parameter is the template we wish to use.
# 
#     return render(request, 'rango/index.html', context_dict)


def about(request):

    context_dict = {'boldmessage': "Rango"}
    return render(request, 'rango/about.html', context_dict)

def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)
