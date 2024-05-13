from django.urls import path
from User import views
app_name="User"
urlpatterns = [

    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('POSTComplaint/',views.POSTComplaint, name="POSTComplaint"),
    path('delComplaint/<int:did>', views.delComplaint,name="delComplaint"),
    path('UserFeedBack/',views.UserFeedBack,name='UserFeedBack'),
    #design
    path('ViewDesignerwork/',views.ViewDesignerwork,name='ViewDesignerwork'),
    path('index/',views.index,name="index"),
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),
    path('review/',views.review,name="review"),
    
]