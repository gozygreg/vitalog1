from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

def index(request):
    return render(request, 'home/index.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            'Welcome to Vitalog:' + message_name, #email subject
            message,
            message_email, # from or sender's email
            ['community.vitalog@gmail.com'], # email patient is sending to
            fail_silently=False,
        )

        messages.success(
            request,
            "Thank you, Your email sent successfully! We will get back to you shortly",
        )

        return redirect("index")

    else: 
        #return page
        return render(request, 'home/contact.html', {})