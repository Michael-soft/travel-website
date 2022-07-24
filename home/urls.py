from django.urls import path
from .views import home

app_name = "home"

urlpatterns = [
    
    path("", home, name="index"), 
#     path("about/", about, name="about"),
#     path("contact/", contact, name="contact") 
    
]
