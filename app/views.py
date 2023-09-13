from django.shortcuts import get_object_or_404, render,redirect
from .models import register,Report,Solution
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def base(request):
    return render(request,'base.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass1')

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                login(request, user)
                return redirect('home')
        except User.DoesNotExist:
            pass

        return render(request, 'userlogin.html', {'key': "Account credentials do not match"})
    return render(request, 'userlogin.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin')
        else:
            return render(request, 'adminlogin.html', {'key':'Account Not found'})

    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('admin')

    return render(request, 'adminlogin.html')


def admin(request):
    return render(request, 'admin.html')


def logoutt(request):
    logout(request)
    return redirect('base')

def signup(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        p1 = request.POST.get('pass1')
        p2 = request.POST.get('pass2')
        email = request.POST.get('email')

        if p1 == p2:
            if User.objects.filter(username=uname).exists():
                return render(request, 'signup.html', {'key': "User already exists"})
            else:
                user = User.objects.create_user(username=uname, password=p1, email=email)
                reg = register.objects.create(
                    user=user,
                    username=uname,
                    password=p1,
                    email=email,
                )
                subject = 'Registration Confirmation'
                message = 'Thank you for registering  on cyber security help support.'
                from_email = 'athulas733@gmail.com'
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list)
                login(request, user)
                return render(request, 'home.html', {'user': user})
        else:
            return render(request, "signup.html", {'key': 'Passwords do not match'})

    return render(request, 'signup.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contactus.html')

def report(request):
    if request.method == 'POST':
        issue_faced = request.POST.get('issue')
        device_caused = request.POST.get('device')
        screenshot = request.FILES.get('screenshot')
        other_details = request.POST.get('other-details')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')

        report = Report(
            issue_faced=issue_faced,
            device_caused=device_caused,
            screenshot=screenshot,
            other_details=other_details,
            email=email,
            phone_number=phone_number
        )
        report.save()

        subject = 'Your report  has been sent'
        message = f'Thank you for reporting. Your issue willbe addressed by our staff and will contact you soon. For further information and assistance, please contact cybersecurity@gmail.com'
        from_email = 'athulas733@gmail.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)
        return redirect('reportconfirm')

    return render(request, 'report.html')


def solution(request):
    solutions = Solution.objects.all()
    return render(request, 'solution.html', {'solutions': solutions})

def addsolution(request):
    if request.method == 'POST':
        image = request.FILES['image']
        problem = request.POST['problem']
        chances = request.POST['chances']
        precautions = request.POST['precautions']
        solutions = request.POST['solutions']
        advisor = request.POST['advisor']
        solution = Solution(image=image, problem=problem, chances=chances, precautions=precautions, solutions=solutions, advisor=advisor)
        solution.save()

        return redirect('admin')

    return render(request, 'addsolution.html')

def reportconfirm(request):
    return render(request,'reportconfirm.html')

@login_required
def viewreports(request):
    reports = Report.objects.all()
    username = request.user.username
    return render(request, 'viewreports.html', {'reports': reports, 'username': username})

@login_required
def contact(request, report_id):
    report = get_object_or_404(Report, pk=report_id)  
    
    if request.method == 'POST':
        message = request.POST.get('message')
        images = request.POST.get('images')
        send_mail(
            'cyber security helpline',
            message,
            'athulas733@gmail.com',
            [report.email], 
            fail_silently=False,
        )
        return render(request, 'contactconfirm.html')

    context = {'report': report}
    return render(request, 'contact.html', context)

def contactconfirm(request):
    return render(request,'contactconfirm.html')
 



