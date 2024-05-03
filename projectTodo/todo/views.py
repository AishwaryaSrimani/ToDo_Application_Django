from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from todo.models import task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
# Create your views here.

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2'] 
        
        try:    
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Usermname already exsists change username')
                    return redirect('/register')
                else:
                    user = User.objects.create_user(username=username, password=password1)
                    user.save()
                    messages.info(request, 'Congratulations! User created')
                    return redirect('login')
            else:
                 raise ValueError("Password does not match. Try again...")  
                           
        except ValueError as ve:
            messages.error(request, str(ve))
            return redirect('/register')
        
    else:
        return render(request, 'register.html')



def login(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            
            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                 raise ValueError("Invalid Credentials. Try again...")
                
        except ValueError as ve:
            messages.info(request, str(ve))
            return redirect('/login')
        
    else:
        return render(request, 'login.html')
    
    
    
def addTodo(request):
   
    if request.method == 'POST':
        try:
            taskTitle = request.POST['taskTitle']
            taskDesc = request.POST['taskDesc']
            username = request.POST['username']
            
            if User.objects.filter(username=username).exists():
                tasks = task.objects.create(taskTitle=taskTitle, taskDesc=taskDesc, username=username)
                tasks.save()
                return redirect('/todoList')
            else:
                raise ValueError("Invalid Username. Try again...")
        
        except ValueError as ve:
            messages.info(request, str(ve))
            return redirect('/addTodo')
        
    else:
        return render(request, 'addTodo.html')




def todoList(request):
    user_tasks = task.objects.filter(username=request.user.username)
    context = {'tasks': user_tasks}
    return render(request, 'todoList.html', context)
    
    
    
def task_update(request, task_id):
    if request.method == 'POST':
        new_task_desc = request.POST.get('new_task_desc')
        task_object = get_object_or_404(task, id=task_id)           # Retrieve the task object using the task ID
        
        task_object.taskDesc = new_task_desc                         # Update the task description
        task_object.save()
        return redirect('/todoList')
    else:
        task_object = get_object_or_404(task, id=task_id)           # Retrieve the task object using the task ID
        context = {'task': task_object}                             # Pass the task object to the template
        
        return render(request, 'task_update.html', context)
    
    
def delete_task(request, task_id):
    task_object = get_object_or_404(task, id=task_id)
    task_object.delete()
    return redirect('/todoList')
    
    
def logout(request):
    auth.logout(request)
    return redirect('/')



def change_password(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        new_password = request.POST['new_password'] 
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist. Try again...')
            return redirect('/change_password')
        
        if not user.check_password(password):
            messages.error(request, 'Incorrect Password. Try again...')
            return redirect('/change_password')
        
        user.password = make_password(new_password)
        user.save()
        
        messages.success(request, 'Password changed successfully')
        return redirect('/login')
        
    else:
        return render(request, 'update.html')
    