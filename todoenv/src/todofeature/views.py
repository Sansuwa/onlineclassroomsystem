from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from todofeature.models import Task
from todofeature.forms import TaskForm
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
#class TaskCreateView(LoginRequiredMixin, CreateView)--for class based view if we have to use login required


# Create your views here.

# class TodoForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = "__all__"



def todo_list_view(request):
    tasks = Task.objects.all().order_by("id")
    context = {"tasks": tasks}
    return render(request,"todo_list.html",context)

@login_required
def todo_add_views(request):
    form = TaskForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return HttpResponseRedirect(reverse("todofeature:todo_list"))       
    return render(request,"add_todo.html",{"form": form})


def todo_edit_view(request, taskid):
    task = get_object_or_404(Task, id = taskid)
    # try:
    #     Task.objects.get(id=taskid)
    # except Task.DoesNotExist:
    #     raise Http404()    
    form = TaskForm(request.POST or None, request.FILES or None, instance=task)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("todofeature:todo_list"))       
    return render(request,"add_todo.html",{"form": form})


def todo_delete_view(request):
    taskid = request.POST.get("taskid")
    task = get_object_or_404(Task, id = taskid)
    task.delete()
    return HttpResponseRedirect(reverse("todofeature:todo_list")) 

def demo_for_ajax(request):
    data = {"name":"Ram","Address":"Kathmandu"}
    return JsonResponse(data,safe=False)

    
    
