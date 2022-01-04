from django.shortcuts import render
from django.views import View
# Create your views here.

class HomePage(View):
    def get(self, request):
        context = {}
        return render(request,template_name="home.html", context=context)
    def post(self, request):
        pass    