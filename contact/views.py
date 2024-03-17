from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def contact(request):
    # A view to contact
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Message from School Website" 
			body = {
			'name': form.cleaned_data['name'],  
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@school.com', ['admin@school.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("home")
      
	form = ContactForm()
	return render(request, "contact/contact.html", {'form':form})

