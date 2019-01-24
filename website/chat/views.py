import json

from django.shortcuts import render, \
    get_object_or_404  # later get_object_or_404   will be used for try except avoidance
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.safestring import mark_safe
from django.views import generic
from django.views.generic import View
from .forms import UserForm


class UserFormView(View):
    form_class = UserForm
    template_name = 'register.html'                 # registration form

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']        # checks username & password
            password = form.cleaned_data['password']

            user.set_password(password)                     # checks user is present or not
            user.save()                                     # save into superuser field

            # return render(request, 'regSuccess.html')             # new added

            # login
            user = authenticate(username=username, password=password)   #

            if user is not None:

                if user.is_active:
                    login(request, user)
                    # login(user)
                    # return redirect('music:register')
                    # return render('regSuccess.html')
                    # return render(request, 'regSuccess.html')  # best and executed
                    return render(request, 'regSuccess.html')
                    # return render(None, 'regSuccess.html')
                    # return redirect('<h1> reg success')

        return render(request, self.template_name, {'form': form})
        #return HttpResponse("done")

# obj = UserFormView()


# def log_in(request):
#     form_class = UserForm
#     template_name = 'registartion/login.html'
#     form = form_class(request.POST)
#     username = form.cleaned_data['username']
#     print(username)
#     password = form.cleaned_data['password']
#     print(password)
#     user = authenticate(username=username, password=password)
#
#     if user is not None:
#
#         if user.is_active:
#             login(request, user)
#             #login(user)
#             #return redirect('music:register')
#         # return render('regSuccess.html')
#             #return render(request, 'loginSuccess.html')
#             return render(request, 'regSuccess.html')# best and executed
#         # return render(None, 'regSuccess.html')
#         # return redirect('<h1> reg success')

class log_in(View):                             # for login purpose
    form_class = UserForm
    template_name = 'registartion/login.html'

    # form = form_class(request.POST)
    # username = form.cleaned_data['username']
    # print(username)
    # password = form.cleaned_data['password']
    # print(password)
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:
                login(request, user)
                # login(user)
                # return redirect('music:register')
                # return render('regSuccess.html')
                # return render(request, 'loginSuccess.html')
                return render(request, 'regSuccess.html')  # if crediantials matches
                                                        # go to this html page
        # return render(None, 'regSuccess.html')
        # return redirect('<h1> reg success')
        # return HttpResponse("done")     # new added

# def chat(request):
#     return HttpResponse("<h1>chat body</h1>")


def index(request):
    return render(request, 'index.html', {})


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
