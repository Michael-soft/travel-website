from django.urls import path
from .views import  passwordrecovery, passwordupdate, serviceterms, signup,signin,myaccount,terms,landing, termsup
from home.views import home, about, contact, service,blog,privacypol,notify

app_name = "accounts"

urlpatterns = [
    
    path("signup/", signup, name="signup"),
    path("landing/", landing, name="landing-page-after-sign-in"), 
    path("signin/", signin, name="signin"),
    path("", home, name="index"), 
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"), 
    path("notification/", notify, name="notification"),
    path("service/", service, name="service"),
    path("terms/", terms, name="terms-and-policies"),
    path("tofs/", serviceterms, name="terms-of-service"),
    path("terms-signup/", termsup, name="terms-and-policies-signup"),
    path("blog/", blog, name="blog"),
    path("my-account/", myaccount, name="my-account"),
    path("privacy-policy/", privacypol, name="privacy-policy"),
    path("passupdate/", passwordupdate, name="passwordupdate"), 
    path("passrecovery/", passwordrecovery, name="passwordrecovery"),
]