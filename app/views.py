from django.shortcuts import render
from .models import Home,About,Testimonial,Service,PortfolioItem,Contact,Skill


def home(request):
    banner = Home.objects.first()
    abouts = About.objects.all()
    testimonials = Testimonial.objects.all()
    services = Service.objects.all()
    portfolioItems = PortfolioItem.objects.all()
    contacts = Contact.objects.all()
    skills = Skill.objects.all()
    

    context = {
        'banner':banner,
        'abouts':abouts,
        'testimonials':testimonials,
        'services':services,
        'portfolioItems':portfolioItems,
        'contacts':contacts,
        'skills':skills

    }

    return render(request,'index.html',context)


def service(request):
    return render(request,'service-details.html')