from django.shortcuts import render
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
        pass    