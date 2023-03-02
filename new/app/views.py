from django.shortcuts import render,get_object_or_404,redirect
from . models import test
from .forms import testform
# Create your views here.

def formpage(request):
    form = testform()
    if request.method == 'POST':
      form = testform(request.POST, request.FILES)
      if form.is_valid():
            form.save()
            form = testform()
    return render(request,'formpage.html',{'form':form})



def Update(request, id):
    objs = test.objects.get(id=id)
    form = testform()
    if request.method =='POST':
        form = testform(request.POST, instance = objs)
        if form.is_valid():
            form.save()
            form = testform() 
            return redirect('details')

    return render(request,'update.html',{'form':form, 'objs':objs})



def details(request):
    obj = test.objects.all()
    return render(request,'details.html',{'obj':obj})

def viewpage(request, pk):
    objs = test.objects.get(pk=pk)
    # objs = get_object_or_404(test, id=id)
    return render(request,'view.html',{'objs':objs})

def delete(request, pk):
    deletes = test.objects.get(pk=pk)
    if request.method == 'POST':
        deletes.delete()
        return redirect('details')
    return render(request,'delete.html',{'deletes':deletes})
