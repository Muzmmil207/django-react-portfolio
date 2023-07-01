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
        subject = "My Portfolio"
        message = template.render({"contact": instance})
        email = EmailMessage(
            subject,
            message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.RECIPIENT_ADDRESS],
        )
        email.get_connection()
        email.send()
