from django.shortcuts import render,redirect,HttpResponse
from. models import User
from.forms import UserForm

# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def output(request):
    return render(request,'details.html')
def dep(request):
    if request.method == "POST":
        form=UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/information")
            except:
                pass
    else:
        form=UserForm()
    return render(request,'details.html',{'form':form})
def information(request):
    userData=User.objects.all()
    return render(request,'information.html',{'userData':userData})
def edit(request,id):
    userData=User.objects.get(id=id)
    return render(request,'edit.html',{'userData':userData})
def update(request,id):
    userData=User.objects.get(id=id)
    form=UserForm(request.POST,instance=userData)
    if form.is_valid():
        form.save()
        return redirect('/information')
    return render(request, 'edit.html', {'userData': userData})
def delete(request,id):
    userData=User.objects.get(id=id)
    userData.delete()
    return redirect('/information')

