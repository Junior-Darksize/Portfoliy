from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Home(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=100),
        text=models.CharField(max_length=300),
    )
    image = models.ImageField(upload_to='Home/')


    
    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "Home"


class About(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=150),
        short_description=models.CharField(max_length=150),
        Birthday=models.CharField(max_length=60),
        Age=models.IntegerField(),
        Website=models.CharField(max_length=60),
        Degree = models.CharField(max_length=60),
        Phone = models.CharField(max_length=60),
        Email = models.CharField(max_length=70),
        City = models.CharField(max_length=70),
        Freelance = models.CharField(max_length=70),
        text = models.TextField()
    )
    image = models.ImageField(upload_to='About/')



    def __str__(self):
        return self.title



class PortfolioItem(models.Model):
    image = models.ImageField(upload_to='portfolio_images/')


class Service(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200),
        description=models.TextField(),
    )

    def __str__(self):
        return self.title


class Testimonial(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100),
        position=models.CharField(max_length=100),
        message=models.TextField(),
    )
    image = models.ImageField(upload_to='testimonial_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    

class Contact(TranslatableModel):
    translations = TranslatedFields(
        address=models.CharField(max_length=255),
        phone_number=models.CharField(max_length=20),
        email=models.EmailField(),
    )

    def __str__(self):
        return f"{self.email}"

class Skill(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=50),
        skill=models.IntegerField(),
    )

    def __str__(self):
        return f"{self.name}"


