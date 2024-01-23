from django.shortcuts import render
from django.http import HttpResponse
    
from . models import *
from . forms import BookingForm
from .forms import ContactForm

# Create your views here.
# def index(request):
#     return HttpResponse("hello world")
# def about(request):
#     return HttpResponse("about page")
# def booking(request):
#     return HttpResponse("booking page")
# def doctors(request):
#     return HttpResponse("doctors page")
# def contact(request):
#     return HttpResponse("contact page")
# def department(request):
#     return HttpResponse("department page")

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def booking(request):
    form=BookingForm
    dict_form={
        'forms':form
    }
    return render(request,"booking.html",dict_form)


def doctor(request):
    dict_doc={
        'doctors':Doctors.objects.all()
    }
    return render(request,"doctors.html",dict_doc)

def contact(request):
    return render(request,"contact.html")

def department(request):
    return render(request,"department.html")


# tags if -else
def index(request):
    person={
        'name':'jhon',
        'age':20
    }
    return render(request,"index.html",person)

def index(request):
    person={
        'name':'jhon',
        'age':20
    }
    # numbers={
    #     'num1':20
    # }
    # return render(request,"index.html",numbers)

    numbers={
    'num1':[1,2,3,4,5,6]
    }
    return  render(request,"index.html",numbers)


def department(request):
    dict_dep={
        'dept':Department.objects.all()
    }
    return render(request, 'department.html',dict_dep)

def doctors(request):
    dict_doc={
        'doc':Doctors.objects.all()
    }
    return render(request, 'doctors.html',dict_doc)


def contact_view(request):
    if request .method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.savr()
            return render(request,'contact.html')
        
        else:form = ContactForm()
        return render(request,'contact.html',{'form':form})