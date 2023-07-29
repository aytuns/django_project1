from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .models import ContactInfo

from django.core.mail import EmailMessage
from contactpage.settings import EMAIL_HOST_USER
from fpdf import FPDF
import sys

# Create your views here.

class ContactForm(View):
	def post(self, request):
		fullname = request.POST['fullname']
		phone = request.POST['phonenumber']
		myemail = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		location = request.POST['location']
        
		contact_create = ContactInfo.objects.create(fullname=fullname,
                                                    phone=phone,
                                                    email=myemail,
                                                    message=message,
                                                    location=location,
                                                    subject=subject )
    	
		contact_create.save()
		

		pdf = FPDF()
        	# Add a PDF page
		pdf.add_page()

		# set font & fill style (using local font style due to unicode character formatting issues)
		pdf.add_font('Arial','',r"C:\Windows\Fonts\arial.ttf",uni=True)
		pdf.set_font('Arial', size=15)

		pdf.cell(w=100,h=10,txt=f"Hello {fullname}, see details of your form",new_x='LMARGIN', new_y='NEXT',center=True)
		pdf.cell(w=0,h=10,new_x='LMARGIN', new_y='NEXT')

		pdf.cell(w=180,h=10,new_x='LMARGIN', new_y='NEXT',
			txt=f"Name: {fullname}")
		pdf.cell(w=180,h=10,new_x='LMARGIN', new_y='NEXT',
			txt=f"Phone number: {phone}")
		pdf.cell(w=180,h=10,new_x='LMARGIN', new_y='NEXT',
			txt=f"Email address: {myemail}")
		pdf.cell(w=180,h=10,new_x='LMARGIN', new_y='NEXT',
			txt=f"Location: {location}")
		pdf.cell(w=180,h=10,new_x='LMARGIN', new_y='NEXT',
			txt=f"Subject of your message: {subject}")
		pdf.multi_cell(w=180,h=10,new_x='LMARGIN', new_y='NEXT',
			txt=f"Your message: {message}")

		pdfOutput = f'{fullname}.pdf'
		pdf.output(pdfOutput)

		sendemail = EmailMessage(subject,
			      				"YOUR REQUEST HAS BEEN NOTED",
								EMAIL_HOST_USER,
            					[myemail] )
		sendemail.attach_file(pdfOutput)
		sendemail.send()

		return HttpResponse(f"Hello {fullname}, your Message has been sucessfully created. Go back to send another message")

	def get(self, request):
		return render(request, 'index.html')
    
