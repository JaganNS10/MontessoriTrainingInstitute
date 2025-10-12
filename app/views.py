from django.shortcuts import render,redirect

from twilio.rest import Client
from django.contrib import messages
import os


def Home(request):
    return render(request,'index.html')


def About(request):
    return render(request,'about.html')


def Academics(request):
    return render(request,'academics.html')


def Admissions(request):
    return render(request,'Admissions.html')

def Campus_facilities(request):
    return render(request,'campus-facilities.html')

def Faculty_staff(request):
    return render(request,'faculty-staff.html')


def Contact(request):
    if request.method == "POST":
        data = request.POST
        message = f"HELLO ADMIN NEW USER ASK FOR HELP!:)\nName: {data.get("name")}\nEmail: {data.get("email")}\nPhone: {data.get("phone")}\nSubject: {data.get("subject")}\nMessage: {data.get("message")}"
        print(message)

        account_sid = os.getenv('ACCOUNT_SID')
        auth_token = os.getenv('AUTH_TOKEN')
        Twilio_api = Client(account_sid,auth_token)
        From = "+18152474413"
        to = ["+91 7904136090"]

        for i in to:
            send_msg = Twilio_api.messages.create(
                body=message,
                from_=From,
                to=to
            ) 
        messages.success(request,f'We Call Your Back {data.get("name")} Best Regards by Montessori Training Institute...')
        return redirect('Home')

    return render(request,'contact.html')


def Error(request):
    return render(request,'404.html')
# Create your views here.
