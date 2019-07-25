from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    context = {'todos':TodoItem.objects.all()}
    return render(request,'todo/todo.html',context=context)

def addtodo(request):

    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')
def deletetodo(request,todo_id):
    item_to_delete=TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
