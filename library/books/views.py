from django.shortcuts import render
from books.models import book
from books.forms import Bookform
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')


@login_required
def addbook(request):
    if(request.method=="POST"):
        t = request.POST['t']
        a = request.POST['a']
        p = request.POST['p']
        f = request.FILES['f']
        i = request.FILES['i']
        b = book.objects.create(title=t,author=a,price=p,pdf=f,cover=i)
        b.save()
        return viewbook(request)
    return render(request,'addbook.html')

@login_required
def viewbook(request):
    k=book.objects.all()
    return render(request,'viewbook.html',{'b':k})


@login_required
def addbook1(request):  #built in form
    if(request.method=='POST'):#after form submission
        form=Bookform(request.POST,request.FILES)#creates form object initialize with values insdie request.POST
        if form.is_valid():
            form.save()  #saves the form object inside Db table
        return viewbook(request)

    form=Bookform()     #creates empty form object with no values
    return render(request,'addbook1.html',{'form':form})


@login_required
def bookdetail(request,p):
    b=book.objects.get(id=p)
    return render(request,'bookdetail.html',{'b':b})


@login_required
def bookdelete(request,p):
    b=book.objects.get(id=p)
    b.delete()
    return viewbook(request)


@login_required
def bookedit(request,p):
    b=book.objects.get(id=p)
    if(request.method=='POST'):#after form submission
        form=Bookform(request.POST,request.FILES,instance=b)
        if form.is_valid():
            form.save()  #saves the form object inside Db table
        return viewbook(request)

    form=Bookform(instance=b)
    return render(request,'edit.html',{'form':form})



def search(request):
    query=""
    b=None
    if(request.method=="POST"):
        query=request.POST['q']
        if (query):
            b=book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))

    return render(request,'search.html',{'query':query,'b':b})










# FACTORIAL
def fact(request):
    if (request.method == 'POST'):
        n=int(request.POST['n'])
        f=1
        for i in range(1,n+1):
            f=f*i
        return render(request,'fact.html',{'fact':f})
    return render(request,'fact.html')




