'''
views.py - это файл, который содержит все представления Django.

FBV - это функции представления Django.
CBV - это классы представления Django.
'''

from django.shortcuts import render, HttpResponse


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello, World!')


def main_view(request):
   mock_data = [
       {
                'id': 1,
                'title': "I'm blue da ba dee da ba daa",
                'description': "Мем про синего человека",
                'created_at': "2022-01-01",
        },
        {
            'id': 2,
            'title': "Doge",
            'description': "Мем про собаку",
            'created_at': "2022-01-02",
        },
        {
            'id': 3,
            'title': "Pepe the Frog",
            'description': "Мем про лягушку",
            'created_at': "2022-01-03",
        }
    ]
   
   if request.method == 'GET':
       return render(request, 'main.html', {'mock_data': mock_data})

    