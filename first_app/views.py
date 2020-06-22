from django.shortcuts import render
from first_app.models import AccessLog, User
from .forms import UsersForm, UserSignIn, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    return render(request, "index.html")

def register(request):

    registered = False

    if request.method == "POST":

        user_form = UserSignIn(request.POST)
        profile_form = UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

        else:

            print(user_form.errors, profile_form.errors)

    else:

        user_form = UserSignIn()
        profile_form = UserProfileInfoForm()

    return render(request, "register.html",
                                            {"user_form": user_form,
                                             "profile_form": profile_form,
                                             "registered": registered})

def user_login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request, user)
                return HttpResponseRedirect(reverse('first_app:forms'))

            else:

                return HttpResponse("Account Not Active")

        else:

            return HttpResponse("Invalid Login Credentials")

    else:

        return render(request, 'index.html', {})

@login_required
def user_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def home(request):

    access_list = AccessLog.objects.order_by('date')
    log_dir = {"access_records": access_list}
    return render(request, 'home.html', context=log_dir)

@login_required
def help(request):

    help_dir = {"help":"HTML Template taged from folder"}
    return render(request, 'help.html', context=help_dir)

@login_required
def users(request):

    users = User.objects.order_by('first_name')
    users_dir = {"users": users}
    return render(request, 'users.html', context=users_dir)

@login_required
def form_name(request):

    form = UsersForm()

    if request.method == 'POST':

        form_data = UsersForm(request.POST)

        if form_data.is_valid():

            form_data.save(commit = True)
            return users(request)

    # if request.method == 'POST':
    #     form_post = forms.FormName(request.POST)
    #
    #     if form_post.is_valid():
    #
    #         print("Validated")
    #         print(form_post.cleaned_data['name'])
    #         print(form_post.cleaned_data['email'])
    #         print(form_post.cleaned_data['verify_email'])
    #         print(form_post.cleaned_data['text'])

    form_dir = {"form": form}
    return render(request, 'forms.html', context=form_dir)
