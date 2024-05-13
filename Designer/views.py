from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render
from User.models import *
from Guest.models import *
from django.db.models import Q
from datetime import datetime
from Designer.models import *
# Create your views here.

def homepage(request):
    return render(request,"Designer/HomePage.html")

def my_pro(request):
    data=tbl_designer.objects.get(id=request.session["dsid"])
    return render(request,"Designer/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_designer.objects.get(id=request.session["dsid"])
    if request.method=="POST":
        prodata.designer_name=request.POST.get('txtname')
        prodata.designer_contact=request.POST.get('txtcon')
        prodata.designer_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Designer/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Designer/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_designer.objects.filter(id=request.session["dsid"],designer_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_designer.objects.get(id=request.session["dsid"],designer_password=request.POST.get('txtcurpass'))
                userdata.designer_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"Designer/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Designer/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Designer/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Designer/ChangePassword.html")
    
def DesignerFeedBack(request):
    data=tbl_feedback.objects.filter(designer=request.session["dsid"])
    designerID=tbl_designer.objects.get(id=request.session["dsid"])
    if request.method=="POST":
        subject=request.POST.get('txtsubject')
        details=request.POST.get('txtdetails')
        tbl_feedback.objects.create(feedback_subject=subject,feedback_details=details,designer=designerID)
        return redirect("Designer:DesignerFeedBack")
    else:
        return render(request,"Designer/DesignerFeedBack.html",{"data":data})
    
def ajaxCategory(request):
    cat = tbl_category.objects.get(id=request.GET.get("did"))
    subcategory = tbl_place.objects.filter(category=cat)
    return render(request,"Designer/AjaxCategory.html",{"subcategory":subcategory})
    
def Designerwork(request):
    designerID = tbl_designer.objects.get(id=request.session["dsid"])
    categorydata = tbl_category.objects.all()
    subcategorydata = tbl_subcategory.objects.all()
    materialdata = tbl_material.objects.all()
    colordata = tbl_color.objects.all()
    designerdata = tbl_designer.objects.all()
    data = tbl_designerwork.objects.all()
    if request.method == "POST":
        # subcatName=request.POST.get('txtname')
        cat=tbl_category.objects.get(id=request.POST.get("sel_category"))
        subcat=tbl_subcategory.objects.get(id=request.POST.get("sel_subcategory"))
        met=tbl_material.objects.get(id=request.POST.get("sel_material"))
        col=tbl_color.objects.get(id=request.POST.get("sel_color"))
        tbl_designerwork.objects.create(work_details=request.POST.get('txtdet'),designerwork_photo=request.FILES.get('fileImage'),designerwork_rate=request.POST.get('txtrate'),designerwork_duration=request.POST.get('txtdur'),subcategory=subcat,material=met,color=col,category=cat,designer=designerID)
        return render(request,"Designer/DesignerWork.html",{'data':data,'categorydata':categorydata,'subcategorydata':subcategorydata,'materialdata':materialdata,'colordata':colordata,'designerdata':designerdata})
    else:
        return render(request,"Designer/DesignerWork.html",{'data':data,'categorydata':categorydata,'materialdata':materialdata,'subcategorydata':subcategorydata})
    

def DesignerGallery(request, id):
    data = tbl_gallery.objects.all()
    # designer_id = request.session.get("dsid")
    designer_id = tbl_designerwork.objects.get(id=id)
    # designer  = tbl_designer.objects.get(id=designer_id)
    if request.method == "POST":
        gallery = request.POST.get("txtgallery")
        gallerycap = request.POST.get("txtcap")
        tbl_gallery.objects.create(designerwork_id=designer_id,gallery_file=gallery,gallery_caption=gallerycap)
        return render(request,"Designer/Gallery.html",{'data':data})
    else:
        return render(request,"Designer/Gallery.html")

    
def ajaxSubcategory(request):
    cat = tbl_category.objects.get(id=request.GET.get("did"))
    subcategory = tbl_subcategory.objects.filter(category=cat)
    return render(request,"Designer/AjaxSubcategory.html",{"subcategorydata":subcategory})

def ajaxColor(request):
    met = tbl_material.objects.get(id=request.GET.get("did"))
    col = tbl_color.objects.filter(material=met)
    return render(request,"Designer/AjaxColor.html",{"colordata":col})

def index(request):
    return render(request,"Designer/index.html")

def User(request):
    data = tbl_user.objects.filter(user_status=1)
    return render(request,"Designer/User.html",{'data':data})

def ViewUserReview(request):
    data = tbl_review.objects.all()
    return render(request,"Designer/ViewUserReview.html",{'data':data})
    


def chatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"Designer/Chat.html",{"user":user})

def ajaxchat(request):
    file = request.FILES.get("file")
    if file != '':
        if request.POST.get("msg") != '':
            from_user = tbl_designer.objects.get(id=request.session["dsid"])
            to_user = tbl_user.objects.get(id=request.POST.get("tid"))
            tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),designer_from=from_user,user_to=to_user,chat_file=request.FILES.get("file"))
            return render(request,"Designer/Chat.html")
        else:
            from_user = tbl_designer.objects.get(id=request.session["dsid"])
            to_user = tbl_user.objects.get(id=request.POST.get("tid"))
            tbl_chat.objects.create(chat_content="",chat_time=datetime.now(),designer_from=from_user,user_to=to_user,chat_file=request.FILES.get("file"))
            return render(request,"Designer/Chat.html")
    else:
        from_user = tbl_designer.objects.get(id=request.session["dsid"])
        to_user = tbl_user.objects.get(id=request.POST.get("tid"))
        tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),designer_from=from_user,user_to=to_user,chat_file="")
        return render(request,"Designer/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_designer.objects.get(id=request.session["dsid"])
    chat_data = tbl_chat.objects.filter((Q(designer_from=user) | Q(designer_to=user)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Designer/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(designer_from=request.session["dsid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(designer_to=request.session["dsid"]))).delete()
    return render(request,"Designer/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})