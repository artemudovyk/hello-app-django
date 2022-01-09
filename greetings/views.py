from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.utils import IntegrityError
from .forms import GreetingForm
from .models import Greeting
from django.urls import reverse


def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GreetingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            email = form.cleaned_data['email']
            try:
                new_greeting = Greeting.objects.create(email=email)
                messages.success(request, f'Hello {email}!')
                return HttpResponseRedirect(reverse('greetings:history'))
            except IntegrityError:
                messages.error(request, f'Already greeted you {email}!')
                form = GreetingForm()
                
            # return HttpResponseRedirect('/greetings')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = GreetingForm()
        
    context = {
        'form': form,
    }

    return render(request, 'greetings/home.html', context)
    
    
def greetings_history(request):
    greetings = Greeting.objects.all()
    print(greetings)
    
    context = {
        'greetings': greetings,
    }
    return render(request, 'greetings/who-came-before-you.html', context)