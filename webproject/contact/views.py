from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage


# Create your views here.


def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            content = request.POST.get("content")

            email_content = EmailMessage(
                "Message from web1_django",
                f"The user with name {name}, with the email {email}, write the following: \n\n{content}",
                "",
                ["piwero@gmail.com"],
                reply_to=[email],
            )
            try:
                email_content.send()

                return redirect("/contact/?valid")

            except:
                return redirect("/contact/?invalid")

    return render(request, "contact/contact.html", {"my_form": contact_form})
