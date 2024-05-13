from django.urls import path,include
from Admin import views

app_name="WebAdmin"

urlpatterns = [

    path('admin/',views.adminInsertSelect,name='adminInsertSelect'),
    path('deladmin/<int:did>',views.deladmin,name='deladmin'),
    path('adminUpdate/<int:eld>',views.adminUpdate,name='adminUpdate'),

    path('District/',views.districtInsertSelect,name="districtInsertSelect"),
    path('delDistrict/<int:did>',views.delDistrict,name="delDistrict"),
    path('districtUpdate/<int:eld>',views.districtUpdate,name="districtUpdate"),

    path('category/',views.categoryInsertSelect,name="categoryInsertSelect"),
    path('delCategory/<int:did>',views.delCategory,name="delCategory"),
    path('categoryUpdate/<int:eld>',views.categoryUpdate,name="categoryUpdate"),

    path('Subcategory/',views.SubcategoryInsertSelect,name="SubcategoryInsertSelect"),
    path('delSubcategory/<int:did>',views.delSubcategory,name="delSubcategory"),
    path('UpdateSubcategory/<int:eld>',views.UpdateSubcategory,name="UpdateSubcategory"),

    path('color/',views.colorInsertSelect,name="colorInsertSelect"),
    path('delColor/<int:did>',views.delColor,name="delColor"),
    path('colorUpdate/<int:eld>',views.colorUpdate,name="colorUpdate"),

    path('material/',views.materialInsertSelect,name='materialInsertSelect'),
    path('delmaterial/<int:did>',views.delmaterial,name="delmaterial"),
    path('materialUpdate/<int:eld>',views.materialUpdate,name="materialUpdate"),
    # path('place/',views.place)

    #place
    path('place/',views.placeInsertSelect,name="placeInsertSelect"),
    path('delplace/<int:did>',views.delPlace,name="delPlace"),
    path('placeUpdate/<int:eld>',views.placeUpdate,name="placeUpdate"),

    #user

    path('HomePage/',views.LoadingHomePage,name='LoadingHomePage'),
    path('userListNew/',views.userListNew,name='userListNew'),
    path('acceptuser/<int:aid>',views.acceptuser,name="acceptuser"),
    path('rejectuser/<int:rid>',views.rejectuser,name="rejectuser"),
    path('UserListAccepted/',views.userListAccepted,name="userListAccepted"),
    path('UserListRejected/',views.userListRejected,name="userListRejected"),
    path('UserComplaintListNew/',views.UserComplaintListNew,name="UserComplaintListNew"),
    path('UserComplaintReply/<int:cid>',views.UserComplaintReply,name="UserComplaintReply"),
    path('ViewUserReview/',views.ViewUserReview,name="ViewUserReview"),

    path('UserFeedBackList/',views.UserFeedBackList,name="UserFeedBackList"),
    path('UserFeedBackView/<int:fid>',views.UserFeedBackView,name="UserFeedBackView"),

    #Designer

    path('HomePage/',views.LoadingHomePage,name='LoadingHomePage'),
    path('designerListNew/',views.designerListNew,name='designerListNew'),
    path('acceptdesigner/<int:aid>',views.acceptdesigner,name="acceptdesigner"),
    path('rejectdesigner/<int:rid>',views.rejectdesigner,name="rejectdesigner"),
    path('DesignerListAccepted/',views.DesignerListAccepted,name="DesignerListAccepted"),
    path('DesignerListRejected/',views.DesignerListRejected,name="DesignerListRejected"),

    path('DesignerFeedBackList/',views.DesignerFeedBackList,name="DesignerFeedBackList"),
    path('DesignerFeedBackView/<int:fid>',views.DesignerFeedBackView,name="DesignerFeedBackView"),


    path('HomePage/',views.HomePage,name="HomePage"),
    
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('index/',views.index,name="index"),
]
