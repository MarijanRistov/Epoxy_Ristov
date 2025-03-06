from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.conf import settings
from .forms import ContactForm
from django.shortcuts import render

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']  # Корисничка е-пошта
            telnum = form.cleaned_data['telnum']  # Телефонски број
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Создавање на полнотекстуално тело на пораката
            full_message = f"Name: {name}\nE-Mail: {email}\nTel-Nummer: {telnum}\n\nNachricht:\n{message}"

            try:
                # Создавање на EmailMessage објект
                email_message = EmailMessage(
                    subject,
                    full_message,
                    settings.EMAIL_HOST_USER,  # Вашиот email
                    ['beschichtung.ristov@gmail.com'],  # Примач на email
                    headers={'Reply-To': email}  # Додадете Reply-To
                )
                email_message.send(fail_silently=False)
                return JsonResponse({"message": "Erfolg"}, status=200)
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)
        else:
            return JsonResponse({"error": form.errors.as_json()}, status=400)
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})


def datenschutzerklarung(request):
    return render(request, 'datenschutzerklarung.html')

def impressum(request):
    return render(request, 'impressum.html')
# Home
def index(request):
    return render(request, 'index.html')

# Bodenbeschichtungen
def bodenbeschichtungen(request):
    return render(request, 'bodenbeschichtungen.html')

# Wandbeschichtungen
def wandbeschichtungen(request):
    return render(request, 'wandbeschichtungen.html')

# Abdichtungen
def abdichtungen(request):
    return render(request, 'abdichtungen.html')

# Untergrundvorbereitung
def untergrundvorbereitung(request):
    return render(request, 'untergrundvorbereitung.html')

# Unsere Arbeiten (Gallery)
def gallery(request):
    return render(request, 'gallery.html')

# About Us (Company Info)
def about_us(request):
    return render(request, 'about-us.html')
