from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .models import ContactInfo
from django.core.mail import EmailMessage
from contactpage.settings import EMAIL_HOST_USER
from fpdf import FPDF
from django.template.loader import get_template

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

		# Save file to local directory
		pdfOutput = f'{fullname}.pdf'
		pdf.output(f"PDFdownloads/{pdfOutput}","F")

		#Create methods to send email to user and admin

		# Retrieve templates from template folder
		htmlMail_user = get_template('send_to_user.html')
		htmlMail_admin = get_template('send_to_admin.html')
		htmlResponse = get_template('user_response.html')
		content = {'subject':subject,'fullname':fullname}

		html_content_user = htmlMail_user.render(content)
		html_content_admin = htmlMail_admin.render(content)
		user_response = htmlResponse.render(content)

		# Send mails
		sendEmail_user = EmailMessage(f"Message: {subject}",
			    				html_content_user,
								EMAIL_HOST_USER,
            					[myemail] )
		sendEmail_user.send()

		sendEmail_admin = EmailMessage(f"New Message: {subject}",
			      				html_content_admin,
								EMAIL_HOST_USER,
            					['aythingy@gmail.com'] )
		sendEmail_admin.attach_file(f"PDFdownloads/{pdfOutput}")
		sendEmail_admin.send()		

		return HttpResponse(user_response)

	def get(self, request):
		return render(request, 'index.html')
