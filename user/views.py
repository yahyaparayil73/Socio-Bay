from django.shortcuts import render,redirect
from user.models import User
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.


def user_home(request):
    if request.method == 'POST':
        user = 'Yahya'
        html = render_to_string(
            template_name = 'chat_history.html',
            context = {'user_name': user}
        )
        return JsonResponse({'html':html})
    return render(request, 'user_home.html')


def user_login(request):
    msg = ''
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        # try:
        user = User.objects.get(
            user_email=email, user_password=password)  # model_name= post_name
        request.session['user_id'] = user.id
        msg = 'Success '+ user.user_name
        return redirect('user:user_home')
        # except Exception as e:
            # print(e)  # to check error
            # msg = 'Invalid credentials'
    return render(request, 'login.html', {'message': msg})


def user_profile(request):
    return render(request, 'user_profile.html')


def user_signup(request):
    if request.method == "POST":
        
        user_name = request.POST['user_name']

        user_email = request.POST['user_email']
        user_password = request.POST['user_password']

        new_user = User(user_name = user_name, user_email=user_email,
        user_password=user_password)

        new_user.save()  # corresponding query of insert
        return redirect('user:user_login')
    return render(request, 'signup.html')


def user_statistics(request):
    return render(request, 'user_statistics.html')


def user_complaints(request):
    return render(request, 'user_complaints.html')


def test(request):
    return render(request, 'test.html')


def user_change_password(request):
    return render(request, 'user_change_password.html')


def chat(request):
    return render(request, "chat.html")


def room(request):
    return render(request, "room.html")

def chat_history(request):
    return render(request, "chat_history.html")
