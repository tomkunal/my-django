from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import Todo
from .forms import TodoForm

def index(request):
    todo_list = Todo.objects.order_by('id')

    form = TodoForm()

    context = {'todo_list' : todo_list, 'form' : form}

    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')

def render_game(request):
    return render(request, 'todo/game.html')

def timekunal(request):
    feature_part = request.GET.get('featurePart')
    #sheet1.write(1,0,feature_part)
    f=open('untitled1.txt','a+')
    f.write(feature_part+"\n")
    #ls.append(feature_part)
    #ls=[feature_part]
    
    #df=pd.DataFrame([feature_part])
    #df.to_excel("output2.xlsx")
    print(feature_part)
    return JsonResponse("kunal", safe=False)
def timeroll(request):
    
    feature_part = request.GET.get('featurePart')
    #sheet1.write(1,0,feature_part)
    f=open('untitled3.txt','a+')
    f.write(feature_part+"\n")
    #ls.append(feature_part)
    #ls=[feature_part]
    
    #df=pd.DataFrame([feature_part])
    #df.to_excel("output2.xlsx")
    print(feature_part)
    
    return JsonResponse("kunal", safe=False)

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')
