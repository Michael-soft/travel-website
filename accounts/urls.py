from django.urls import path
from .views import signup

app_name = "accounts"

urlpatterns = [
    
    path("", signup, name="signup"), 
    # path("about/", about, name="about"),
    # path("contact/", contact, name="contact") 
    
]