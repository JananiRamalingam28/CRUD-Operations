from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import d



def home(request):
    mydata=d.objects.all()
    if(mydata!=""):
        return render(request,"index.html",{"d":mydata})
    else:
        return render(request,"index.html")
def addData(request):
    if request.method=="POST":
        firstN=request.POST["FN"]
        lastN=request.POST["LN"]
        userN=request.POST["user"]
        emailN=request.POST["email"]
        contactN=request.POST["contact"]
        passwordN=request.POST["password"]
        cpassN=request.POST["cpass"]

        obj=d()
        obj.FN=firstN
        obj.LN=lastN
        obj.user=userN
        obj.email=emailN
        obj.contact=contactN
        obj.password=passwordN
        obj.cpass=cpassN
        obj.save()
        mydata=d.objects.all()
        return redirect("home")
    return render (request,"index.html")

def updateData(request,id):
    mydata=d.objects.get(id=id)
    if request.method=="POST":
        firstN=request.POST["FN"]
        lastN=request.POST["LN"]
        userN=request.POST["user"]
        emailN=request.POST["email"]
        contactN=request.POST["contact"]
        passwordN=request.POST["password"]
        cpassN=request.POST["cpass"]

        mydata.FN=firstN
        mydata.LN=lastN
        mydata.user=userN
        mydata.email=emailN
        mydata.contact=contactN
        mydata.password=passwordN
        mydata.cpass=cpassN
        mydata.save()
        return redirect("home")
    return render(request,"update.html",{"data":mydata})

def deleteData(request,id):
    mydata=d.objects.get(id=id)
    mydata.delete()
    return redirect("home")





# Create your views here.
