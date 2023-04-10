from django.shortcuts import redirect, render
from socio_admin.models import Admin


from user.models import Complaint,User

# Create your views here.

def admin_home(request):
    return render(request,'admin_home.html')

def admin_login(request):
    msg = ''
    if request.method == 'POST':
        aname = request.POST['a_name']
        apassword = request.POST['a_password']
        try:

            new_admin = Admin.objects.get(
                a_name = aname, 
                a_password = apassword)                                   # model_name= post_name
            request.session['user'] = new_admin.id                           # creation of session id for admin
            return redirect('socio_admin:admin_home')
        
        except Admin.DoesNotExist:
            msg = 'Invalid credentials'
    return render(request,'admin_login.html',{'msg':msg})

def view_complaints(request):
    complaints = Complaint.objects.all()
    return render(request,'view_complaints.html',{'complaints':complaints})

def viewUsers(request):
    users = User.objects.all()
    return render(request,'view_users.html',{'users':users})