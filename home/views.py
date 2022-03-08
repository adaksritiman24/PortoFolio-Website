import imp
from django.contrib import messages
from .models import Message
from django.shortcuts import redirect, render
from django.views import View
from .models import Project
# Create your views here.


class HomePage(View):
    def get(self, request):
        projects = Project.objects.all()[:6]
        project_list = []
        for project in projects:
            project_list.append(
                {"title":project.title, 
                "desc": project.desc[:120]+"...",
                "image": project.image,
                "date": project.date,
                "link":project.link,
                }
            )
        context = {
            'projects':project_list,
        }
        return render(request,template_name="home.html", context=context)
 
    def post(self, request):
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        message = request.POST['message']

        message = Message(fname = fname, lname = lname, email = email, message = message)
        message.save()
        messages.success(request,"Your message was sent successfully");

        return redirect('/')   