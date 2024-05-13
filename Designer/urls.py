from django.urls import path
from Designer import views

app_name="Designer"

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('DesignerFeedBack/',views.DesignerFeedBack,name='DesignerFeedBack'),
    path('Designerwork/',views.Designerwork,name='Designerwork'),
    path('DesignerGallery/<int:id>',views.DesignerGallery,name='DesignerGallery'),

    path('ajaxSubcategory/',views.ajaxSubcategory,name='ajaxSubcategory'),
    path('ajaxColor/',views.ajaxColor,name='ajaxColor'),

    path('index/',views.index,name="index"),
    path('User/',views.User,name="User"),

    path('ViewUserReview/',views.ViewUserReview,name="ViewUserReview"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),
]