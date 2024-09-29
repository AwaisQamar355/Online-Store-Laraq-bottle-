from django.shortcuts import render,HttpResponse,redirect
from home.models import Product,Shop,Homeone,Purification,Drinkware
from datetime import datetime
from home.models import Contact,Home
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login , logout
from home.models import Corporate,Larq
from math import ceil
from home.models import Orders,Update,Tracker
import json
from home.models import Signup
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
import razorpay

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRECT))
# from home.models import Orders
import json
# Create your views here.
def home(request):
    Products = Product.objects.all()
    print(Products)
    n = len(Products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range' : range (1,nSlides),  'product' : Products}

    if request.method == "POST":
        email = request.POST.get("email")
        home = Home(email = email , date = datetime.today())
        home.save()
        messages.success(request, "Thank You!")

    return render(request, 'home.html',params)
def homeone(request):
    Products = Homeone.objects.all()
    print(Products)
    n = len(Products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range' : range (1,nSlides),  'product' : Products}
    
    return render(request , 'homeone.html' , params)


def accessries(request):
    return render(request , 'accessries.html')

def corporate(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        company = request.POST.get("company")
        subject = request.POST.get("subject")
        textarea = request.POST.get("textarea")
        corporate = Corporate(name = name , phone = phone ,  email = email , subject = subject ,
                               company = company , textarea = textarea , date = datetime.today())
        corporate.save()
    
    return render(request , 'corporate.html')
def drinkware(request):
    Products = Drinkware.objects.all()
    print(Products)
    n = len(Products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range' : range (1,nSlides),  'product' : Products}
    
    return render(request , 'drinkware.html' , params)
def exploreall(request):
    return render(request , 'exploreall.html')
def faq(request):
    return render(request , 'faq.html')
def hydrations(request):
    return render(request , 'hydrations.html')
def loginuser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request, user)
            return redirect("home.html")
        else:
            return redirect("signup.html")

    return render(request , 'login.html')
def logoutuser(request):
    logout(request)
    return render(request , 'logout.html')
def signup(request):
    HttpResponse("Hello Welcome to your home page")
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        repeatpassword = request.POST.get("repeatpassword")
        
        sign = Signup(username=username , email = email , password =  password , repeatpassword = repeatpassword ,date = datetime.today())
        sign.save()

        if User.objects.filter(username = username).exists():
            error_message = 'Username already taken. Please choose a different username.'
            return render(request , 'signup.html' ,{'error_message' : error_message})
        
        if password != repeatpassword:
            return HttpResponse("Your Password and confirm password are not the same!")
        
        else:
            myuser = User.objects.create_user(username,email,password)
            myuser.save()
        return redirect('login.html')
    return render(request,'signup.html')

def purification(request):
    Products = Purification.objects.all()
    print(Products)
    n = len(Products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range' : range (1,nSlides),  'product' : Products}

    
    return render(request , 'purification.html', params)
def shopall(request):
    Products = Shop.objects.all()
    print(Products)
    n = len(Products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range' : range (1,nSlides),  'product' : Products}
    
    return render(request , 'shopall.html', params)
def shophome(request):
    return render(request , 'shophome.html')
def technology(request):
    return render(request , 'technology.html')

def purevis(request):
    return render(request , 'purevis.html')
def nanozero(request):
    return render(request , 'nanozero.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        textarea = request.POST.get("textarea")

        contact = Contact(name = name , email = email , subject = subject , textarea = textarea , date = datetime.today())
        contact.save()
        messages.success(request, "Thank You!")

        # subject = subject
        # textarea = textarea
        # from_email = settings.EMAIL_HOST_USER
        # try:
        #     send_mail(subject, textarea, from_email, ["arhamkhann437@gmail.com"])
        #     return redirect('home')
        # except:
        #     return redirect('contact.html')

        # subject = request.POST.get("subject", "")
        # subject = request.POST.get("subject", "")
        # from_email = request.POST.get("from_email", "")
        # try:
        #     send_mail(subject, subject, from_email, ["awaisqamar321@gmail.com"])
        #     return redirect('home.html')
        # except BadHeaderError:
        #     return redirect('contact.html')
        # return HttpResponse("Make sure all fields are entered and valid.")
        
    return render(request , 'contact.html')

def retailer(request):
    return render(request , 'retailer.html')


def press(request):

    return render(request , 'press.html')

def ourstory(request):

    return render(request , 'ourstory.html')

def larq(request):
    if request.method == "POST":
        email = request.POST.get("email")
        larq = Larq(email = email , date = datetime.today())
        larq.save()
    return render(request , 'larq.html')

def affilite(request):

    return render(request , 'affilite.html')

def swing(request):

    return render(request , 'swing.html')


def pure(request):

    return render(request , 'pure.html')
def larqpure(request):

    return render(request , 'larqpure.html')
def larqpicture(request):

    return render(request , 'larqpicture.html')
def larqswing(request):

    return render(request , 'larqswing.html')
def larqfilter(request):

    return render(request , 'larqfilter.html')
def larqtwist(request):

    return render(request , 'larqtwist.html')



def reviews(request):

    return render(request , 'reviews.html')



def magzine(request):

    return render(request , 'magzine.html')
def tracker(request):
    HttpResponse("Hello Muhammad Awais welcome too pressPage")

    if request.method == "POST":
        orderid = request.POST.get('orderid')
        email = request.POST.get('email')
        try:
            order = Orders.objects.filter(order_id=orderid, email=email)
            if len(order)>0:
                update = Update.objects.filter(order_id=orderid)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates,order[0].itemsJson] , default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
        # tracker = Tracker(orderid=orderid , email = email)
        # tracker.save()
    
   
    return render(request,'tracker.html')



def checkout(request):
    if request.method == "POST":
        itemsJson = request.POST.get('itemsJson', '')
        # amount = request.POST.get('amount','')
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        country = request.POST.get('country')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        checkbox1 = request.POST.get('checkbox1')
        paymentMethod = request.POST.get('paymentMethod')
        cardname = request.POST.get('cardname')
        cardnumber = request.POST.get('cardnumber')
        expiration = request.POST.get('expiration')
        cvv = request.POST.get('cvv')
        order = Orders(itemsJson = itemsJson ,name = name , lastname = lastname , username=username , email=email , address=address , address2 = address2,
                            country = country , state = state , zip = zip , checkbox1 = checkbox1  , 
                            paymentMethod = paymentMethod  , cardname = cardname , cardnumber = cardnumber , 
                            expiration = expiration , cvv = cvv ,  date = datetime.today())
        order.save()
        update = Update(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'checkout.html', {'thank':thank, 'id': id})

        payment = client.order.create({
            "amount": 1000,
            "currency": "PKR",
            "payment_capture": "1"
        })
        print(payment)
    

    return render(request,'checkout.html')
   

    




def trackorder(request):
    # HttpResponse("Hello Muhammad Awais welcome too pressPage")
    
    return render(request,'trackorder.html')

def allreviews(request):
    return render(request , 'allreviews.html')


















