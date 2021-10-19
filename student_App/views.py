from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import groupProjectsForm
from .models import groupProjects


#Add/create method
def projectForm(request):
    context={}
    form = groupProjectsForm(request.POST or None)
    groupproject  = groupProjects.objects.all()
    if form.is_valid():
       form.save()
    context['form']= form
    return render(request, "projectForm.html",context)
  
  
#home Page/ Retrieve task list
def showlist(request):
    groupproject = groupProjects.objects.all()
    return render(request, "showlist.html",{'groupproject':groupproject})


# Update a single task
def update(request, id):
    groupproject = get_object_or_404(groupProjects, id=id)
    groupproject = groupProjects.objects.get(id=id)
    form = groupProjectsForm(request.POST, instance=groupproject)
    if request.method == "POST":
       if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    context = {
        'form': form,
        'groupproject':groupproject
        }
    return render(request, 'update.html',context)


# delete method
def delete(request,id):
     form = groupProjects.objects.get(id=id)
     form.delete()
     return HttpResponseRedirect('/')
    
    