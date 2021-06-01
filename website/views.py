from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
import requests

# Create your views here.

def home(request):
    return render(request,'website/home.html')

def about(request):
    return render(request,'website/about.html')

def solutions(request):
    return render(request,'website/solutions.html')

def news(request):
    return render(request,'website/news.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email_address = form.cleaned_data['email_address']
            response = requests.get("https://isitarealemail.com/api/email/validate",params = {'email': email_address})
            subject = "Website Inquiry"
            status = response.json()['status']
            if status == "valid": 
                body = {
                'first_name': form.cleaned_data['first_name'], 
                'last_name': form.cleaned_data['last_name'], 
                'email': form.cleaned_data['email_address'],
                'phone_number': form.cleaned_data['phone_number'],  
                'message':form.cleaned_data['message'], 
                }
                message = "\n".join(body.values())

                try:
                    send_mail(subject, message, 'sales@irrokeys.de', ['djebab.toufik@irrokeys.com','belkadi.adel@irrokeys.com']) 
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect ("home")
            
            else :
                print('not a valid email')
        
    form = ContactForm()
    return render(request, "website/contact.html", {'form':form})