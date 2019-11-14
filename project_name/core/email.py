from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_mail(template, to_email, subject, context={}, attachments=None):
    try:
        body = render_to_string(template, context)
        message = EmailMultiAlternatives(subject, body, settings.DEFAULT_FROM_EMAIL, to_email)

        if attachments:
            message.attachments = attachments

        message.attach_alternative(body, "text/html")
        return {'ok': message.send()}
    except Exception as e:
        return {'error': e.args[0]}
