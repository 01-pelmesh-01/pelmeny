from django.shortcuts import render , redirect
from django.views.generic import CreateView , UpdateView , TemplateView , FormView
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.http import HttpResponse , JsonResponse
from .models import CustomUser , story
from django.conf import settings
import random
from django.core.mail import send_mail
from django.contrib.auth.views import PasswordResetView , PasswordResetDoneView , PasswordResetConfirmView , PasswordResetCompleteView
import stripe

def like_mech (x):  
    ID = x.POST.get ('to_like');
    if 'to_like' in x.POST:  
        
        for el in story.objects.all() :
            if int(ID) == int (el.id) :

                if el in x.user.like.all():
                    x.user.like.remove(el) ; el.like_amount -= 1    
                    
                else:
                    x.user.like.add(el) ; el.like_amount += 1 
                    
                           
def generate_code():
    random.seed()
    return str(random.randint(10000,99999))

def home(request):
    ur = request.build_absolute_uri('')[:-1]
    if request.is_ajax():      
        data = {'ur': ur, 'age': 40} 
        print("AAAAAAAAAAA") 
        print(request.GET.get('result', None))
        print(request.GET.get("result_2"))
        return JsonResponse(data)
    else:
        # Обычный HTTP-запрос
        return render(request, 'users/home.html')

def lenta(x):
    if x.is_ajax():     
        #like_mech (x)
        print("AAAAAAAAA")
        data = {'name': 'John', 'age': 28}
        return JsonResponse(data)   
    else:         
        STORY = story.objects.all()       
        s_data = [el.id for el in x.user.like.all()]
        return render(x , "users/lenta.html" , {'story': STORY , 's_data' : s_data})

class signup(FormView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = 'users/signup.html'

    def form_valid(self , form):
        print(CustomUser.objects.filter(is_active=False)) 
        form.save()
        uska , creat = CustomUser.objects.get_or_create(email=form.cleaned_data["email"])
        uska.code = generate_code() ; uska.save()
        link ="go to the link : " + self.request.build_absolute_uri('/') + "endreg" + '?link=' + str(uska.code) 
        send_mail(
            "email confirmation",
            link,
            settings.DEFAULT_FROM_EMAIL,
            [form.cleaned_data["email"]],
            fail_silently=False ,
                )
        
        return super().form_valid(form)

def endreg(x):
    mes = ""
    Link = x.GET.get('link') ; print(Link)    
    user = CustomUser.objects.get(code=Link)
    user.is_active = True ; user.save() ; user.code = "0"
    mes = "Всё идеет по плануу!"
    return render(x, 'users/endreg.html', {'mes': mes})

    
def Login(x):
    mes = "введите логин и пароль"
    if x.method == 'POST':
        form = LoginForm(x.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(x, user)
                    return redirect('home') 
                else:
                    mes = "Выполните подтверждение через почту"
                    return render(x, 'users/login.html', {'form': form , 'mes': mes})

            elif (CustomUser.objects.filter(username=cd['username'] , password=cd['password']).exists()):
                mes = "Выполните подтверждение через почту"
                return render(x, 'users/login.html', {'form': form , 'mes': mes})
            elif (CustomUser.objects.filter(username=cd['username']).exists()):
                mes = "неверный пароль и\или не выполнено подтверждение через почту"
                return render(x, 'users/login.html', {'form': form , 'mes': mes})
            else:
                mes = "пользователь не существует"
                return render(x, 'users/login.html', {'form': form , 'mes': mes})
    else:
        form = LoginForm()
    return render(x, 'users/login.html', {'form': form , 'mes': mes})

class password_reset(PasswordResetView):
    template_name = "users/password.html"
    success_url = reverse_lazy('password2')
    #email_template_name = 'users/password_email.html'

class password_reset2(PasswordResetDoneView):
    template_name = "users/password2.html"

class password_reset3(PasswordResetConfirmView):
    template_name = "users/password3.html"
    success_url = reverse_lazy('users/home.html')

class edit(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("home")
    template_name = 'users/edit.html'

    def get_object(self):
        return self.request.user

def new_post(x): 

    if x.is_ajax():
        DATA = {'name': 'John', 'age': 28}

        if x.method == 'POST':
            form = story_f(x.POST)
            if form.is_valid():
                Name = form.cleaned_data["name"]
                Desc = form.cleaned_data["desс"]
                Image = form.cleaned_data["image"]
                STORY = story.objects.create(name = Name , desс = Desc , image = Image, creator = x.user)
                STORY.save()
                
        return JsonResponse(DATA)
    else:
        form = story_f()
        return render(x, 'users/new_post.html', {'form': form})

def premium(x):
        return render(x, 'users/premium.html')






#print("---->" , x.user.like.all())
    #if story.objects.get(name="ДОМЕСТОС") in x.user.like.all():
    #    print("AAAAAAAAAAAAAAAA")
    #print("--->",x.build_absolute_uri('')[:-1])