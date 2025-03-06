"""
URL configuration for MarijanApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from MarijanProject import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MarijanProject.views import contact_view
urlpatterns = [
    path("admin/", admin.site.urls),
    path('contact/', contact_view, name='contact'),
    path('', views.index, name='home'),  # Home
    path('bodenbeschichtungen/', views.bodenbeschichtungen, name='bodenbeschichtungen'),  # Bodenbeschichtungen
    path('wandbeschichtungen/', views.wandbeschichtungen, name='wandbeschichtungen'),  # Wandbeschichtungen
    path('abdichtungen/', views.abdichtungen, name='abdichtungen'),  # Abdichtungen
    path('untergrundvorbereitung/', views.untergrundvorbereitung, name='untergrundvorbereitung'),  # Untergrundvorbereitung
    path('gallery/', views.gallery, name='gallery'),
    path('impressum/', views.impressum, name='impressum'),
    path('datenschutzerklarung/', views.datenschutzerklarung, name='datenschutzerklarung'),
    path('about-us/', views.about_us, name='about_us'),  # Kontakt

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
