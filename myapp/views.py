from django.shortcuts import render, redirect
from .models import Person

# Create your views here.
def index(request):
    person = Person.objects.all()
    return render(request, 'myapp/index.html', {'person': person})

def add_person(request):
    if request.method == "POST":
        p = request.POST
        add = Person.objects.create(name=p['name'], age=p['age'])
        add.save()
        return redirect('index')
    else:
        return render(request, 'myapp/add_person.html')