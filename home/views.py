
from django.shortcuts import render,redirect

from home.models import Contact, Subscribtion,Post

# Create your views here.


def home(request):
    return render(request, "home/index.html") 

def about(request):
        if request.method=='POST':
           email = request.POST.get("email")
           enter= Subscribtion(email=email)
           enter.save()
           return redirect("home:index")
        return render(request, "home/about.html") 

def aboutus(request):
    if request.method=='POST':
           email = request.POST.get("email")
           enter= Subscribtion(email=email)
           enter.save()
           return redirect("home:index")
    return render(request, "home/about-dubai.html") 

def blog(request):
    posts = Post.objects.all().order_by("-timestamp")
    context ={
             "posts":posts    }
    return render(request, "home/blog.html") 

def contact(request):
    if request.method=='POST':
           fullname = request.POST.get("Name")
           email = request.POST.get("email")
           phone= request.POST.get("phone")
           message= request.POST.get("text")
           enter= Contact(fullname=fullname,email=email,phone=phone,message=message)
           enter.save()
           return redirect("home:index")
    return render(request, "home/contact.html") 

def service(request):
     if request.method=='POST':
           email = request.POST.get("email")
           enter= Subscribtion(email=email)
           enter.save()
           return redirect("home:index")
     return render(request, "home/service.html")

def notify(request):
        if request.method=='POST':
           email = request.POST.get("email")
           enter= Subscribtion(email=email)
           enter.save()
           return redirect("home:index")
        return render(request, "home/notification.html")

def france(request):
        if request.method=='POST':
           email = request.POST.get("email")
           enter= Subscribtion(email=email)
           enter.save()
           return redirect("home:index")
        return render(request, "home/france.html")
 
def eiffel(request):
        if request.method=='POST':
           email = request.POST.get("email")
           enter= Subscribtion(email=email)
           enter.save()
           return redirect("home:index")
        return render(request, "home/eiffel-tower.html")
    
def burj1(request):
        if request.method=='POST':
           email = request.POST.get("email")
           enter= Subscribtion(email=email)
           enter.save()
           return redirect("home:index")
        return render(request, "home/burj-khalifa-1.html")
    
def burj2(request):
        if request.method=='POST':
           email = request.POST.get("email")
           enter= Subscribtion(email=email)
           enter.save()
           return redirect("home:index")
        return render(request, "home/burj-khalifa-2.html")
    
def burj(request):
        if request.method=='POST':
           email = request.POST.get("email")
           enter= Subscribtion(email=email)
           enter.save()
           return redirect("home:index")
        return render(request, "home/burj-khalifa.html")

def leader(request):
        if request.method=='POST':
           email = request.POST.get("email")
           enter= Subscribtion(email=email)
           enter.save()
           return redirect("home:index")
        return render(request, "home/leader.html")

def paris1(request):
        if request.method=='POST':
           email = request.POST.get("email")
           enter= Subscribtion(email=email)
           enter.save()
           return redirect("home:index")
        return render(request, "home/paris-gallery-1.html")

def paris2(request):
        if request.method=='POST':
           email = request.POST.get("email")
           enter= Subscribtion(email=email)
           enter.save()
           return redirect("home:index")
        return render(request, "home/paris-gallery-2.html")

def dtravelguide(request):
        if request.method=='POST':
           email = request.POST.get("email")
           enter= Subscribtion(email=email)
           enter.save()
           return redirect("home:index")
        return render(request, "home/dubai-travel-guide.html")

def abDubai(request):
        if request.method=='POST':
           email = request.POST.get("email")
           enter= Subscribtion(email=email)
           enter.save()
           return redirect("home:index")
        return render(request, "home/about-dubai.html")
  
def faq(request):
        if request.method=='POST':
           email = request.POST.get("email")
           enter= Subscribtion(email=email)
           enter.save()
           return redirect("home:index")
        return render(request, "home/faq-after.html")

def faqBefore(request):
        return render(request, "home/faq-before.html")
 
def privacypol(request):
        if request.method=='POST':
           email = request.POST.get("email")
           enter= Subscribtion(email=email)
           enter.save()
           return redirect("home:index")
        return render(request, "home/privacy-policy.html")

def payment(request):
        if request.method=='POST':
           email = request.POST.get("email")
           enter= Subscribtion(email=email)
           enter.save()
           return redirect("home:index")
        return render(request, "home/payment-confirmation.html")

def checkout(request):
        if request.method=='POST':
           email = request.POST.get("email")
           enter= Subscribtion(email=email)
           enter.save()
           return redirect("home:index")
        return render(request, "home/payment-checkout.html")




