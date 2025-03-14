from django.shortcuts import render
from django.http import JsonResponse

from contact.models import Message


# Create your views here.

def contact(request):
    return render(request, 'contact.html')


def contact_form(request):
    if request.POST:
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

        success = True
        output = 'Contact form sent successfully.'

    else:
        success = False
        output = 'Request method is not valid.'

    context = {
        'success': success,
        'output': output,
    }
    return JsonResponse(context)
