
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import contact

urlpatterns=[
    path("",views.base,name="base"),
    path("base",views.base,name="base"),
    path("ulogin",views.user_login,name="user_login"),
    path("alogin",views.admin_login,name="admin_login"),
    path("signup",views.signup,name="signup"),
    path("home",views.home,name="home"),
    path("about",views.about,name="about"),
    path("contactus",views.contactus,name="contactus"),
    path('contact/<int:report_id>/', contact, name='contact'),
    path("logoutt",views.logoutt,name="logoutt"),
    path("solution",views.solution,name="solution"),
    path("report",views.report,name="report"),
    path("reportconfirm",views.reportconfirm,name="reportconfirm"),
    path("addsolution",views.addsolution,name="addsolution"),
    path("aadmin",views.admin,name="admin"),
    path("viewreports",views.viewreports,name="viewreports"),
    path('viewreports/', views.viewreports, name='viewreports'),
    path("contactconfirm",views.contactconfirm,name="contactconfirm"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
