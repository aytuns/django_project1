from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .models import ContactInfo
from django.core.mail import EmailMessage
from contactpage.settings import EMAIL_HOST_USER
from fpdf import FPDF

# Create your views here.

class ContactForm(View):
	# Function to get details fom the HTML form sending a post request
	def post(self, request):
		fullname = request.POST['fullname']
		phone = request.POST['phonenumber']
		myemail = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		location = request.POST['location']
        
		# Create an instance of the model class to populate the dataBase
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

		# Populate the PDF file with content from the HTML form
		pdf.cell(w=100,h=10,txt=f"MESSAGE FROM {fullname}",new_x='LMARGIN', new_y='NEXT',center=True)
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
			txt=f"Subject of the message: {subject}")
		pdf.multi_cell(w=180,h=10,new_x='LMARGIN', new_y='NEXT',
			txt=f"The message: {message}")

		pdfOutput = f'{fullname}.pdf'
		pdf.output(pdfOutput)

		# Create methods to send email to user and admin
		sendemail1 = EmailMessage(f"Message: {subject}",
			    				f"Hello {fullname} your request has been received.",
								EMAIL_HOST_USER,
            					[myemail] )
		sendemail1.send()

		sendemail2 = EmailMessage(f"New Message: {subject}",
			      				f"New Message from {fullname}, see attachment.",
								EMAIL_HOST_USER,
            					['anything@gmail.com'] )
		sendemail2.attach_file(pdfOutput)
		sendemail2.send()		

		return HttpResponse(f'''
	    	<!DOCTYPE html>
			<html lang="en">
			<head>
			<meta charset="UTF-8">
			<meta http-equiv="X-UA-Compatible" content="IE=edge">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
		    <script src="https://kit.fontawesome.com/0700337eca.js" crossorigin="anonymous"></script>
			<title>MESSAGE SENT</title>
			</head>
			<body style = "margin:auto; padding:5% 0;display:flex;width:90%;text-align:center;background:white">
			<div style = "width:100%; padding: 10px;background:lightblue;">
			<h1>Hello {fullname}, your Message has been sucessfully sent.</h1>
			</div>
			</body>
			</html>
			''')

	def get(self, request):
		return render(request, 'index.html')
