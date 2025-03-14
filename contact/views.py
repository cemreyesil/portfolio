from django.shortcuts import render
from django.http import JsonResponse
from contact.models import Message
from contact.forms import ContactForm


# Create your views here.

def contact_form(request):
    if request.POST:
        contact_form = ContactForm(request.POST or None)

        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            Message.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )

            contact_form.send_email()

            success = True
            output = 'Contact form sent successfully.'
        else:
            success = False
            output = 'Contact form is not valid.'

    else:
        success = False
        output = 'Request method is not valid.'

    context = {
        'success': success,
        'output': output,
    }
    return JsonResponse(context)


def contact(request):
    contact_form = ContactForm()
    context = {
        'contact_form': contact_form,
    }
    return render(request, 'contact.html', context)
