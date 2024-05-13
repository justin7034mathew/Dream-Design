from django.urls import path
from Guest import views
app_name="Guest"

urlpatterns = [

    path('NewUser/',views.userRegistration,name="userRegistration"),
    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
    path('Designer/',views.designerRegistration,name="designerRegistration"),
    path('Login/',views.Login,name="Login"),
    path('index/',views.index,name="index"), 
    
]