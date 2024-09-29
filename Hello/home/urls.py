from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('' , views.home , name = 'home.html'),
    path('home.html' , views.home , name = 'home.html'),
    path('homeone.html' , views.homeone , name = 'homeone.html'),
    path('accessries.html' , views.accessries , name = 'accessries.html'),
    path('checkout.html' , views.checkout , name = 'checkout.html'),
    path('corporate.html' , views.corporate , name = 'corporate.html'),
    path('drinkware.html' , views.drinkware , name = 'drinkware.html'),
    path('exploreall.html' , views.exploreall , name = 'exploreall.html'),
    path('faq.html' , views.faq , name = 'faq.html'),
    path('hydrations.html' , views.hydrations , name = 'hydrations.html'),
    path('login.html' , views.loginuser , name = 'login.html'),
    path('signup.html' , views.signup , name = 'signup.html'),
    path('logout.html' , views.logoutuser , name = 'logout.html'),
    path('purification.html' , views.purification , name = 'purification.html'),
    path('shopall.html' , views.shopall , name = 'shopall.html'),
    path('shophome.html' , views.shophome , name = 'shophome.html'),
    path('technology.html' , views.technology , name = 'technology.html'),
    path('trackorder.html' , views.trackorder , name = 'trackorder.html'),
    path('purevis.html' , views.purevis , name = 'purevis.html'),
    path('nanozero.html' , views.nanozero , name = 'nanozero.html'),
    path('contact.html' , views.contact , name = 'contact.html'),
    path('retailer.html' , views.retailer , name = 'retailer.html'),
    path('press.html' , views.press , name = 'press.html'),
    path('larq.html' , views.larq , name = 'larq.html'),
    path('affilite.html' , views.affilite , name = 'affilite.html'),
    path('ourstory.html' , views.ourstory , name = 'ourstory.html'),
    path('swing.html' , views.swing , name = 'swing.html'),
    path('pure.html' , views.pure , name = 'pure.html'),
    path('larqpure.html' , views.larqpure , name = 'larqpure.html'),
    path('larqpicture.html' , views.larqpicture , name = 'larqpicture.html'),
    path('larqswing.html' , views.larqswing , name = 'larqswing.html'),
    path('larqfilter.html' , views.larqfilter , name = 'larqfilter.html'),
    path('larqtwist.html' , views.larqtwist , name = 'larqtwist.html'),

    path('reviews.html' , views.reviews , name = 'reviews.html'),
    path('magzine.html' , views.magzine , name = 'magzine.html'),
    path('tracker.html' , views.tracker , name = 'tracker.html'),
    path('allreviews.html' , views.allreviews , name = 'allreviews.html'),


]




















