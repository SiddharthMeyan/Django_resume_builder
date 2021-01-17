from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages

from django.http import HttpResponse
from django.views.generic import View

from home.utils import render_to_pdf

def gen_pdf(requests, *args, **kwargs):
    cv = Contact.objects.all().last()
    context = {'cv': cv}
    pdf = render_to_pdf('about.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

def index(requests):
    return render(requests, "index.html")


def about(requests):
    cv = Contact.objects.all().last()
    context = {'cv': cv}
    return render(requests, "about.html", context)


def contact(requests):

    return render(requests, "contact.html")


def cover(requests):
    cv = Contact.objects.all().first() ###########show recent name and attributes

    context = {'cv': cv}
    if requests.method == "POST":

        name = requests.POST.get('name')
        mobile = requests.POST.get('mobile')
        email = requests.POST.get('email')
        twelvep = requests.POST.get('twelvep')
        tenthp = requests.POST.get('tenthp')
        add = requests.POST.get('add')
        skills = requests.POST.get('skills')
        summary = requests.POST.get('summary')
        school = requests.POST.get('school')
        college = requests.POST.get('college')
        masters = requests.POST.get('masters')
        tech = requests.POST.get('tech')
        exp = requests.POST.get('exp')
        contact = Contact(name=name, school=school, college=college, masters=masters, tech=tech, exp=exp,
                          mobile=mobile, add=add, email=email, twelvep=twelvep, tenthp=tenthp, skills=skills, summary=summary)
        contact.save()
    return render(requests, "cover.html", context)
