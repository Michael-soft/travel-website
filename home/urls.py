from django.urls import path
from .views import aboutus, burj, burj1, burj2, checkout, dtravelguide, faqBefore, home, about, blog,leader, contact, paris1, paris2, payment,service,faq,privacypol,abDubai,notify,france,eiffel
from accounts.views import passwordrecovery, passwordupdate, signin, signup,terms,myaccount,landing
app_name = "home"

urlpatterns = [
    
    path("", home, name="index"), 
    path("about/", about, name="about"),
    path("aboutdubai/", aboutus, name="about-dubai"),
    path("blog/", blog, name="blog"),
    path("contact/", contact, name="contact"), 
    path("service/", service, name="service"),
    path("my-account/", myaccount, name="my-account"),
    path("privacy-policy/", privacypol, name="privacy-policy"),
    path("faq-after/", faq, name="faq-after"),
    path("faq-before/", faqBefore, name="faq-before"),
    path("burj/", burj, name="burj-khalifa"),
    path("burj1/", burj1, name="burj-khalifa-1"),
    path("burj2/", burj2, name="burj-khalifa-2"),
    path("paris1/", paris1, name="paris-gallery-1"),
    path("paris2/", paris2, name="paris-gallery-2"),
    path("dubai-travel-guide/", dtravelguide, name="dubai-travel-guide"),
    path("leader/", leader, name="leader"),
    path("terms/", terms, name="terms-and-policies"),
    path("notification/", notify, name="notification"),
    path("eiffel/", eiffel, name="eiffel-tower"), 
    path("about-dubai/", abDubai, name="about-dubai"), 
    path("signup/", signup, name="signup"), 
    path("france/", france, name="france"), 
    path("signin/", signin, name="signin"),
    path("payment/", checkout, name="payment-checkout"),
    path("paymentconfirm/", payment, name="paymentconfirm"),
    path("landing/", landing, name="landing-page-after-sign-in"),
    path("passupdate/", passwordupdate, name="passwordupdate"), 
    path("passrecovery/", passwordrecovery, name="passwordrecovery"),
]
