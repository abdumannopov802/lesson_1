from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail, EmailMessage

# Create your views here.

# def send_email(request):
#     subject = 'Thank you for registering to our site'
#     message = ' it  means a world to us '
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['akromabdumannopov802@gmail.com',]
#     send_mail(subject, message, email_from, recipient_list)
#     return render(request, 'send-email')


from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

def send_email(request):
    subject = request.POST.get("subject", "Some message from subject")
    message = request.POST.get("message", "some message from message")
    from_email = request.POST.get("from_email", "akromabdumannopov815@gmail.com")
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ["akromabdumannopov802@gmail.com",])
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        return HttpResponseRedirect("/contact/thanks/")
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse("Make sure all fields are entered and valid.")


def send_mass_email(request):
    subject = request.POST.get("subject", "Some message from subject")
    message = request.POST.get("message", "some message from message")
    from_email = request.POST.get("from_email", "akromabdumannopov815@gmail.com")
    datatuple = (
        (subject, message, from_email, ["akromabdumannopov802@gmail.com"]),
        (subject, message, from_email, ["akromabdumannopov802@gmail.com"]),
        )
    send_mass_mail(datatuple)
    return render(request, 'send-email')


def send_email_with_file(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['akromabdumannopov802@gmail.com',]
    mail = EmailMessage(subject, message, email_from, recipient_list)
    mail.attach_file('images/send_email_test.jpg')
    mail.attach_file('images/Django_4_By_Example_4th_Edition_Antonio_Mele_Bob_Belderbos_Packt.pdf')
    mail.send()
    return render(request, 'send-email')
