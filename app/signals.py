from django.db.models.signals import post_save,pre_save,pre_delete,post_delete
from django.dispatch import receiver
from .models import Home

@receiver(signal=post_save,sender = Home)
def post_save_about(sender,instance,created,**kwargs):
    
    Home.objects.exclude(id = instance.id).delete()


@receiver(signal=pre_save,sender = Home)
def post_save_banner(sender,instance,**kwargs):

    instance.title = "You can't edit this title"