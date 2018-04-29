from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def home(request):
    title = "Welcome"
    # if request.user.is_authenticated():
    #     title = "My Title %s" % (request.user)

    if request.method == "POST":
        print(request.POST)
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        print instance.email
        print instance.full_name
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full Name"
        instance.full_name = full_name
        instance.save()
        context = {
            "title": "Thank you"
        }

    return render(request, 'home.html', context)


# this is not the model form so we can't save it directly
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key in form.cleaned_data:
        #     print key, form.cleaned_data.get(key)
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_mail = [from_email]
        html_message = """"
            <h1>Hellow</h1>
        """
        contact_message = "%s: %s via %s" %(
            form_full_name,
            form_message,
            form_email
        )
        send_mail(
            subject,
            contact_message,
            from_email, to_mail,
            html_message=html_message,
            fail_silently=True
        )


    # print(request.POST)

    context = {
        "form": form
    }

    return render(request, "forms.html", context)
