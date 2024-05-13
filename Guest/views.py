# Create your views here.
from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.



def userRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(user_name=request.POST.get("txtname"),user_gender=request.POST.get("gender"),user_contact=request.POST.get("txtcontact"),user_email=request.POST.get("txtemail"),user_photo=request.FILES.get("fileImage"),user_proof=request.FILES.get("fileProof"),user_password=request.POST.get("txtpwd"),place=place)
        return redirect("Guest:userRegistration")
    else:
        return render(request,"Guest/NewUser.html",{"districtdata":district})

def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{"placedata":place})

def designerRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place= tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_designer.objects.create(designer_name=request.POST.get("disname"),designer_gender=request.POST.get("disgender"),designer_contact=request.POST.get("discontact"),designer_email=request.POST.get("disemail"),designer_password=request.POST.get("dispwd"),designer_photo=request.FILES.get("fileImage"),designer_proof=request.FILES.get("fileProof"),place=place)
        return redirect("Guest:designerRegistration")
    else:
        return render(request,"Guest/Designer.html",{"districtdata":district})


#Login
 
def Login(request):
    if request.method == "POST":
        usercount = tbl_user.objects.filter(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"),user_status=1).count()
        designercount = tbl_designer.objects.filter(designer_email=request.POST.get("txt_email"),designer_password=request.POST.get("txt_password"),designer_status=1).count()
        admincount = tbl_admin.objects.filter(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password")).count()
        if usercount > 0:
            user = tbl_user.objects.get(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"))
            request.session["uid"] = user.id
            request.session["uname"] = user.user_name
            return redirect("User:index")
        elif designercount > 0:
            designer = tbl_designer.objects.get(designer_email=request.POST.get("txt_email"),designer_password=request.POST.get("txt_password"))
            request.session["dsid"] = designer.id
            request.session["dsname"] = designer.designer_name
            return redirect("Designer:index")
        elif admincount > 0:
            admin = tbl_admin.objects.get(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password"))
            request.session["aid"] = admin.id
            request.session["aname"] = admin.admin_name
            return redirect("WebAdmin:LoadingHomePage")
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
        return render(request,"Guest/Login.html")  
    

def index(request):
    return render(request,"Guest/index.html")
    
