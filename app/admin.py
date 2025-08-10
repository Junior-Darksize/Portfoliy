from django.contrib import admin
from .models import Home,About,PortfolioItem,Service,Testimonial,Contact,Skill
from parler.admin import TranslatableAdmin

@admin.register(Home)
class HomeAdmin(TranslatableAdmin):
    list_display = ('title', 'image')

@admin.register(About)
class AboutAdmin(TranslatableAdmin):
    list_display = ('title', 'short_description', 'Birthday', 'Age', 'Website', 'Degree', 'Phone', 'Email', 'City', 'Freelance')

@admin.register(PortfolioItem)
class PortfolioItemAdmin(TranslatableAdmin):
    list_display = ('image',)

@admin.register(Service)
class ServiceAdmin(TranslatableAdmin):
    list_display = ('title',)

@admin.register(Testimonial)
class TestimonialAdmin(TranslatableAdmin):
    list_display = ('name', 'position', 'message')

@admin.register(Contact)
class ContactAdmin(TranslatableAdmin):
    list_display = ('address', 'phone_number', 'email')

@admin.register(Skill)
class SkillAdmin(TranslatableAdmin):
    list_display = ('name', 'skill')