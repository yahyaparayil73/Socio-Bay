from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from user.models import Complaint, FriendRequest
from user.models import User
from django.http import HttpResponseBadRequest, JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q
from django.http import JsonResponse



# Create your views here.


def user_home(request):
    user = User.objects.get(id=request.session['user'])

    if request.method == 'POST':
        user = 'Irshad PK'
        html = render_to_string(
            template_name='chat_history.html',
            context={'user_name': user}
        )
        return JsonResponse({'html': html})
    return render(request, 'user_home.html', {'user_home_name': user})


def user_login(request):
    msg = ''
    if request.method == 'POST':
        useremail = request.POST['email']
        userpassword = request.POST['password']
        try:

            new_user = User.objects.get(
                user_email=useremail, user_password=userpassword)  # model_name= post_name
            request.session['user'] = new_user.id
            return redirect('user:user_home')
        except User.DoesNotExist:
            msg = 'Invalid credentials'
    return render(request, 'login.html', {'message': msg})


def user_profile(request):
    user = User.objects.get(id=request.session['user'])
    return render(request, 'user_profile.html', {'user_profile': user})


def user_signup(request):
    if request.method == "POST":

        username = request.POST['user_name']
        useremail = request.POST['user_email']
        userimage = request.FILES['user_image']
        userpassword = request.POST['user_password']

        new_user = User(
            user_name=username,
            user_email=useremail,
            user_image=userimage,
            user_password=userpassword)

        new_user.save()  # corresponding query of insert
        return redirect('user:user_login')
    return render(request, 'signup.html')


def user_statistics(request):
    return render(request, 'user_statistics.html')


def user_complaints(request):
    msg = ''
    if request.method == 'POST':

        complaintsubject = request.POST['complaint_subject']
        complaintbody = request.POST['complaint_body']

        user = request.session['user']
        complaints = Complaint(
            complaint_sub=complaintsubject,
            complaint_body=complaintbody,
            users_id=user
        )

        complaints.save()
        msg = 'Complaint recorded Successfully'

    return render(request, 'user_complaints.html', {'message': msg})


def test(request):
    return render(request, 'test.html')


def user_change_password(request):
    msg = ''
    err_msg = ''
    if request.method == 'POST':

        oldpassword = request.POST['user_old_password']
        newpassword = request.POST['user_new_password']
        password = User.objects.get(id=request.session['user'])
        if password.user_password == oldpassword:

            password.user_password = newpassword
            password.save()
            msg = 'Password Updated Successfully'
        else:
            err_msg = 'Passwords does not match'

    return render(request, 'user_change_password.html', {'message': msg, 'error_message': err_msg})


def chat(request):
    return render(request, "chat.html")


def chat_history(request):
    return render(request, "chat_history.html")


def user_requests(request):
    requests = FriendRequest.objects.filter(receiver_id = request.session['user'],status = 'pending')
    print(requests)
    return render(request, "user_requests.html",{'requests':requests})


def add_friend(request):
    return render(request, "add_friend.html")

def user_logout(request):  # to get the sessions deleted after the user logout

    if 'user' in request.session:
        del request.session['user']
    request.session.flush()

    return redirect('user:user_login')


def user_email_exist(request):

    email = request.POST['email_data']
    email_exist = User.objects.filter(user_email=email).exists()

    return JsonResponse({'email_exist': email_exist})


def profile(request):

    user = User.objects.get(id=request.session['user'])

    return render(request, "profile.html", {'user': user})


def sidebar(request):
    return render(request, "sidebar.html")


def search_results(request):
    print("search_results called")
    if request.is_ajax():
        user = request.POST.get('user')
        print(user)
        return JsonResponse({'data': user})
    return JsonResponse({})


def terms_of_use(request):
    return render(request, "terms_of_use.html")


def privacy_policy(request):
    return render(request, "privacy_policy.html")


def search_users(request):
    query = request.POST['query']
    if query:
        users = User.objects.filter(
            Q(user_name__icontains=query) | Q(user_email__icontains=query))
        data = [{'id': user.id, 'username': user.user_name} for user in users]
        return JsonResponse({'users': data})
    else:
        return JsonResponse({})


def show_profile(request, username):
    user = User.objects.get(user_name=username)
    return render(request, "show_profile.html", {'data': user})

def send_friend_request(request):
    if request.method == 'POST':
        reciever_id = request.POST.get('user_id')
        user_id = request.session['user']
        new_request = FriendRequest(

            receiver_id = reciever_id,
            sender_id = user_id,
            status = 'pending'
            
        )
        new_request.save()
    return JsonResponse({'status':True})

def approve_requests(request):
        

        return render(request, "user_requests.html")






