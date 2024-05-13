from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from datetime import date
# Create your views here.

#admin insert and select

def adminInsertSelect(request):
    data = tbl_admin.objects.all()
    if request.method == "POST":
        tbl_admin.objects.create(admin_name=request.POST.get("txtname"),admin_email=request.POST.get("txtemail"),admin_password=request.POST.get("txtpass"))
        return render(request,"Admin/Admin.html",{'data':data})
    else:
        return render(request,"Admin/Admin.html",{'data':data})
    
def deladmin(request,did):
    tbl_admin.objects.get(id=did).delete()
    return redirect("WebAdmin:adminInsertSelect")
    
def adminUpdate(request,eld):
    editdata = tbl_admin.objects.get.all(id=eld) 
    if request.method=="POST":
        editdata.tbl_admin=request.POST.get("txtname")
        editdata.save()
        return redirect("WebAdmin:adminInsertSelect")
    else:
        return render(request,"Admin\Admin.html",{'editdata':editdata})

#insert and select
def districtInsertSelect(request):
    data = tbl_district.objects.all()
    if request.method == "POST":
        disName=request.POST.get('txtname')
        tbl_district.objects.create(district_name=disName)
        return render(request,"Admin/District.html",{'data':data})
    else:
        return render(request,"Admin/District.html",{'data':data})
#delete
def delDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("WebAdmin:districtInsertSelect")
#edit

def districtUpdate(request,eld):
    editdata=tbl_district.objects.get(id=eld)
    if request.method=="POST":
        editdata.district_name=request.POST.get("txtname")
        editdata.save()
        return redirect("WebAdmin:districtInsertSelect")
    else:
        return render(request,"Admin\District.html",{"editdata":editdata})

#category insert and delete
def categoryInsertSelect(request):
    data = tbl_category.objects.all()
    if request.method == "POST":
        catName=request.POST.get('txtname')
        tbl_category.objects.create(category_name=catName)
        return render(request,"Admin/Category.html",{'data':data})
    else:
        return render(request,"Admin/Category.html",{'data':data})

#delete
def delCategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect("WebAdmin:categoryInsertSelect")

#category update
def categoryUpdate(request,eld):
    editdata=tbl_category.objects.get(id=eld)
    if request.method=="POST":
        editdata.category_name=request.POST.get("txtname")
        editdata.save()
        return redirect("WebAdmin:categoryInsertSelect")
    else:
        return render(request,"Admin\Category.html",{"editdata":editdata})
    
#subCategory insert select
    
def SubcategoryInsertSelect(request):
    categorydata = tbl_category.objects.all()
    data = tbl_subcategory.objects.all()
    if request.method == "POST":
        subcatName=request.POST.get('txtname')
        cat=tbl_category.objects.get(id=request.POST.get("sel_category"))
        tbl_subcategory.objects.create(subcategory_name=subcatName,category=cat)
        return render(request,"Admin/Subcategory.html",{'data':data,'categorydata':categorydata})
    else:
        return render(request,"Admin/Subcategory.html",{'data':data,'categorydata':categorydata})
    
#del category
def delSubcategory(request,did):
    tbl_subcategory.objects.get(id=did).delete()
    return redirect("WebAdmin:SubcategoryInsertSelect")

def UpdateSubcategory(request,eld):
    category = tbl_category.objects.all()
    editdata=tbl_subcategory.objects.get(id=eld)
    if request.method=="POST":
        editdata.subcategory_name=request.POST.get("txtname")
        editdata.save()
        cat = tbl_category.objects.get(id=request.POST.get('sel_category'))
        editdata.category = cat
        return redirect("WebAdmin:SubcategoryInsertSelect")
    else:
        return render(request,"Admin/Subcategory.html",{'editdata':editdata,"categorydata":category})


def colorInsertSelect(request):
    materialdata = tbl_material.objects.all()
    data = tbl_color.objects.all()
    if request.method == "POST":
        colorName=request.POST.get('txtname')
        mat = tbl_material.objects.get(id=request.POST.get("sel_material"))
        tbl_color.objects.create(color_name=colorName,material=mat)
        return render(request,"Admin/color.html",{'data':data,'materialdata':materialdata})
    else:
        return render(request,"Admin/color.html",{"data":data,'materialdata':materialdata})
    
#color delete
def delColor(request,did):
    tbl_color.objects.get(id=did).delete()
    return redirect("WebAdmin:colorInsertSelect")
#color update
def colorUpdate(request,eld):
    editdata=tbl_color.objects.get(id=eld)
    if request.method=="POST":
        editdata.color_name=request.POST.get("txtname")
        editdata.save()
        return redirect("WebAdmin:colorInsertSelect")
    else:
        return render(request,"Admin\color.html",{"editdata":editdata})

#material insert select
def materialInsertSelect(request):
    mat = tbl_material.objects.all()
    if request.method == "POST":
        matName=request.POST.get("txtname")
        tbl_material.objects.create(material_name=matName)
        return render(request,"Admin/material.html",{"material":mat})
    else:
        return render(request,"Admin/material.html",{"material":mat})

#material delete
def delmaterial(request,did):
    tbl_material.objects.get(id=did).delete()
    return redirect("WebAdmin:materialInsertSelect")

#material update
def materialUpdate(request,eld):
    editdata = tbl_material.objects.get(id=eld)
    if request.method == "POST":
        editdata.material_name=request.POST.get("txtname")
        editdata.save()
        return redirect("WebAdmin:materialInsertSelect")
    else:
        return render(request,"Admin\material.html",{"editdata":editdata})
    
#place insert delete

def placeInsertSelect(request): 
    district=tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
       placeName=request.POST.get('txtname')
       dis=tbl_district.objects.get(id=request.POST.get("sel_district"))
       tbl_place.objects.create(place_name=placeName,district=dis)
       return render(request,"Admin/place.html",{'data':data,"districtdata":district})
    else:
        return render(request,"Admin/place.html",({'data':data,"districtdata":district}))

def delPlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("WebAdmin:placeInsertSelect")

def placeUpdate(request,eld):
    district = tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=eld)
    if request.method=="POST":
        editdata.place_name=request.POST.get("txtname")
        editdata.save()
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.district = dis
        return redirect("WebAdmin:placeInsertSelect")
    else:
        return render(request,"Admin/place.html",{'editdata':editdata,"districtdata":district})

#Newuser insert delete
    


def LoadingHomePage(request):
    return render(request,"Admin/HomePage.html")


def userListNew(request):
    userdata = tbl_user.objects.filter(user_status=0)
    return render(request,"Admin/UserListNew.html",{'userdata':userdata})

def acceptuser(request,aid):
    user = tbl_user.objects.get(id=aid)
    user.user_status = 1
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def rejectuser(request,rid):
    user = tbl_user.objects.get(id=rid)
    user.user_status = 2
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def userListAccepted(request):
    userdata = tbl_user.objects.filter(user_status=1)
    return render(request,"Admin/UserListAccepted.html",{"userdata":userdata})

def userListRejected(request):
    userdata = tbl_user.objects.filter(user_status=2)
    return render(request,"Admin/UserListRejected.html",{"userdata":userdata})

def UserComplaintListNew(request):
    data=tbl_complaint.objects.filter(complaint_status=0)
    return render(request,"Admin/UserComplaintListNew.html",{'data':data})

def UserComplaintReply(request,cid):
    complaint = tbl_complaint.objects.get(id=cid)
    if request.method == "POST":
        complaint.complaint_replydate = date.today()
        complaint.complaint_reply = request.POST.get('txtreply')
        complaint.complaint_status=1
        complaint.save()
        return render(request,"Admin/UserComplaintReply.html",{'msg':"Replay send"})
    else:

        return render(request,"Admin/UserComplaintReply.html",{'complaint':complaint})
    

def UserFeedBackList(request):
    data=tbl_feedback.objects.filter(feedback_status=0)
    return render(request,"Admin/UserFeedBAckList.html",{'data':data})

def UserFeedBackView(request,fid):
     feedback=tbl_feedback.objects.get(id=fid)
     feedback.feedback_status = 1
     feedback.save()
     return redirect("WebAdmin:UserFeedBackList")

def ViewUserReview(request):
    data = tbl_review.objects.all()
    return render(request,"Designer/ViewUserReview.html",{'data':data})



#New designer accept,reject

def LoadingHomePage(request):
    return render(request,"Admin/HomePage.html")


def designerListNew(request):
    designerdata = tbl_designer.objects.filter(designer_status=0)
    return render(request,"Admin/DesignerListNew.html",{'designerdata':designerdata})

def acceptdesigner(request,aid):
    designer = tbl_designer.objects.get(id=aid)
    designer.designer_status = 1
    designer.save()
    return redirect("WebAdmin:LoadingHomePage")

def rejectdesigner(request,rid):
    designer = tbl_designer.objects.get(id=rid)
    designer.designer_status = 2
    designer.save()
    return redirect("WebAdmin:LoadingHomePage")

def DesignerListAccepted(request):
    designerdata = tbl_designer.objects.filter(designer_status=1)
    return render(request,"Admin/DesignerListAccepted.html",{"designerdata":designerdata})

def DesignerListRejected(request):
    designerdata = tbl_designer.objects.filter(designer_status=2)
    return render(request,"Admin/DesignerListRejected.html",{"designerdata":designerdata})

def DesignerFeedBackList(request):
    data=tbl_feedback.objects.filter(feedback_status=0)
    return render(request,"Admin/DesignerFeedBackList.html",{'data':data})


def DesignerFeedBackView(request,fid):
     feedback=tbl_feedback.objects.get(id=fid)
     feedback.feedback_status = 1
     feedback.save()
     return redirect("WebAdmin:DesignerFeedBackList")

#admin

def HomePage(request):
    return render(request,"Admin/HomePage.html")

def my_pro(request):
    data=tbl_admin.objects.get(id=request.session["aid"])
    return render(request,"Admin/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_admin.objects.get(id=request.session["aid"])
    if request.method=="POST":
        prodata.admin_name=request.POST.get('txtname')
        prodata.admin_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Admin/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Admin/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_admin.objects.filter(id=request.session["aid"],admin_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_admin.objects.get(id=request.session["aid"],admin_password=request.POST.get('txtcurpass'))
                userdata.admin_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"Admin/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Admin/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Admin/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Admin/ChangePassword.html")

def index(request):
    return render(request,"Admin/index.html")