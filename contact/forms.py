from django import forms
from django.conf import settings
from django.core.mail import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=254,
        required=True
    )
    email = forms.EmailField(
        max_length=254,
        required=True
    )
    subject = forms.CharField(
        max_length=254,
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea,
        required=True
    )

    def send_email(self):
        if self.is_valid():
            name = self.cleaned_data['name']
            email = self.cleaned_data['email']
            subject = self.cleaned_data['subject']
            message = self.cleaned_data['message']

            message_context = (f"Name: {name}\n"
                               f"Email: {email}\n"
                               f"Subject: {subject}\n"
                               f"Message: {message}"
                               )

            email = EmailMessage(
                subject=subject,
                body=message_context,
                from_email=email,
                to=[settings.DEFAULT_FROM_EMAIL],
                reply_to=[email],
            )
            email.send()

            return True
