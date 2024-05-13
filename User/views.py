from django.shortcuts import render,redirect
from Guest.models import *
from Designer.models import *

# Create your views here.
from django.shortcuts import render
from User.models import *
from django.db.models import Q
from datetime import datetime
# Create your views here.

def homepage(request):
    return render(request,"User/HomePage.html")

def my_pro(request):
    data=tbl_user.objects.get(id=request.session["uid"])
    return render(request,"User/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        prodata.user_name=request.POST.get('txtname')
        prodata.user_contact=request.POST.get('txtcon')
        prodata.user_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"User/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"User/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_user.objects.filter(id=request.session["uid"],user_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_user.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcurpass'))
                userdata.user_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"User/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"User/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"User/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"User/ChangePassword.html")
    

def POSTComplaint(request):
    data=tbl_complaint.objects.filter(user=request.session["uid"])
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        title=request.POST.get('txttitle')
        details=request.POST.get('txtcomplaint')
        tbl_complaint.objects.create(complaint_title=title,complaint_details=details,user=userID)
        return redirect("User:POSTComplaint")
    else:
        return render(request,"User/UserPOSTComplaint.html",{"data":data})
    
def delComplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("User:POSTComplaint")

def UserFeedBack(request):
    data=tbl_feedback.objects.filter(user=request.session["uid"])
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        subject=request.POST.get('txtsubject')
        details=request.POST.get('txtdetails')
        tbl_feedback.objects.create(feedback_subject=subject,feedback_details=details,user=userID)
        return redirect("User:UserFeedBack")
    else:
        return render(request,"User/UserFeedback.html",{"data":data})
    
def ViewDesignerwork(request):
    designerID = tbl_designer.objects.get(id=request.session["dsid"])
    categorydata = tbl_category.objects.all()
    subcategorydata = tbl_subcategory.objects.all()
    materialdata = tbl_material.objects.all()
    colordata = tbl_color.objects.all()
    designerdata = tbl_designer.objects.all()
    data = tbl_designerwork.objects.filter(designer=request.session["dsid"])
    if request.method == "POST":
        # subcatName=request.POST.get('txtname')
        cat=tbl_category.objects.get(id=request.POST.get("sel_category"))
        subcat=tbl_subcategory.objects.get(id=request.POST.get("sel_subcategory"))
        met=tbl_material.objects.get(id=request.POST.get("sel_material"))
        col=tbl_color.objects.get(id=request.POST.get("sel_color"))
        # tbl_designerwork.objects.create(subcategory=subcat,material=met,color=col,category=cat,designer=designerID)
        data=tbl_designerwork.objects.filter(subcategory=subcat,material=met,color=col,category=cat,designer=designerID)
        return render(request,"User/ViewDesignWork.html",{'data':data,'categorydata':categorydata,'subcategorydata':subcategorydata,'materialdata':materialdata,'colordata':colordata,'designerdata':designerdata})
    else:
        return render(request,"User/ViewDesignWork.html",{'categorydata':categorydata,'materialdata':materialdata,'subcategorydata':subcategorydata})    
    

def index(request):
    return render(request,"User/index.html")
    
def review(request):
    data = tbl_review.objects.all()
    if request.method == "POST":
        tbl_review.objects.create(review_name=request.POST.get('review'),Rating_details=request.POST.get('rating'),Comment_details=request.POST.get('comment'))
        return render(request,"User/UserReview.html")
    else:
        return render(request,"User/UserReview.html")
    

    
# def ReplyCompaint(request):
#     userID=tbl_user.objects.get(id=request.session["uid"])
    
def chatpage(request,id):
    user  = tbl_designer.objects.get(id=id)
    return render(request,"User/Chat.html",{"user":user})

def ajaxchat(request):
    file = request.FILES.get("file")
    if file != '':
        if request.POST.get("msg") != '':
            from_user = tbl_user.objects.get(id=request.session["uid"])
            to_user = tbl_designer.objects.get(id=request.POST.get("tid"))
            tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,designer_to=to_user,chat_file=request.FILES.get("file"))
            return render(request,"User/Chat.html")
        else:
            from_user = tbl_user.objects.get(id=request.session["uid"])
            to_user = tbl_designer.objects.get(id=request.POST.get("tid"))
            tbl_chat.objects.create(chat_content="",chat_time=datetime.now(),user_from=from_user,designer_to=to_user,chat_file=request.FILES.get("file"))
            return render(request,"User/Chat.html")
    else:
        from_user = tbl_user.objects.get(id=request.session["uid"])
        to_user = tbl_designer.objects.get(id=request.POST.get("tid"))
        tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,designer_to=to_user,chat_file="")
        return render(request,"User/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(designer_from=tid) | Q(designer_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(designer_to=request.GET.get("tid")) | (Q(designer_from=request.GET.get("tid")) & Q(user_to=request.session["uid"]))).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})