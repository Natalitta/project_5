from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from .models import Contact

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['contact_email']
            message = form.cleaned_data['message']

            # Create a new Contact object and save it to the database
            contact = Contact.objects.create(
                name=name,
                contact_email=email,
                message=message
            )

            # Send email
            subject = "Message from School Website"
            email_message = f"Name: {name}\nEmail: {email}\nMessage: {message}"

            try:
                send_mail(
                    subject,
                    email_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.EMAIL_HOST_USER]
                )
				# Add success message
                messages.success(request, 'Message sent successfully.')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            # Redirect to home page upon successful form submission
            return redirect("home")

    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {'form': form})
