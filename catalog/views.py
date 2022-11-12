from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html', {
        'page_title': 'Shopping'
    })

