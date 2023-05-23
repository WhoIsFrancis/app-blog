from django.views.generic import View
from django.shortcuts import render

# Vista de clases
class HomeView(View):
    # request es la informacion
    # getRequest pide la informacion que quieres ver
    # postRequest es el que envia la informacion al servidor
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'index.html', context)