from django import forms

# Create your forms here.
from captcha.fields import CaptchaField



class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	phone_number = forms.CharField(max_length = 50)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)
	captcha = CaptchaField()