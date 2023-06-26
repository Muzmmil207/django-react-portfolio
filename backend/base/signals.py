from django.conf import settings
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import loader

from .models import Contact


@receiver(post_save, sender=Contact)
def contact_signals(sender, instance, created, **kwargs):
    if created:
        template = loader.get_template("email.html")
        mail_subject = "My Portfolio"
        message = template.render({"contact": instance})
        to_email = settings.RECIPIENT_ADDRESS
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()
