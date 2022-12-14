from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html', {
        'page_title': 'Main'
    })


def about(request):
    return render(request, 'home/about.html', {
        'page_title': 'About'
    })


def contacts(request):
    return render(request, 'home/contacts.html', {
        'page_title': 'Contacts'
    })
