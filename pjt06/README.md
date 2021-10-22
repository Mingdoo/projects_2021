# pjt06



6번 프로젝트 !

##### 목표

- 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web application 제작
- Django web framework를 통한 데이터 조작
- Authentication(사용자 인증)에 대한 이해



##### 요구사항

- pjt06/은 startproject 명령어로 생성되는 project 디렉토리입니다.
- community/는 startapp 명령어로 생성되는 application 디렉토리입니다.
- 아래의 폴더구조는 주요한 폴더와 파일만 명시되어 있습니다.



```
pjt06/
 settings.py
 urls.py
 ...
templates/
 	base.html
 	
 accounts/
 	migrations/
	templates/
	 	accounts/
	 		*.html
	forms.py
	models.py
	urls.py
	views.py
 ...
community/
 	migrations/
 	templates/
 		community/
 			*.html
 	forms.py
 	models.py
 	urls.py
 	views.py
 	...
manage.py
...

```



##### Model

| 필드명      | 자료형        | 설명               |
| ----------- | ------------- | ------------------ |
| movie_title | String <= 100 | 리뷰한 영화의 제목 |
| title       | String <= 100 | 리뷰의 제목        |
| content     | Text          | 내용               |
| rank        | Integer       | 리뷰한 영화의 평점 |

```python
#in community/models.py
from django.db import models

# Create your models here.
class Review(models.Model):
    movie_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.IntegerField()
```



##### Form

```python
#in community/forms.py
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta():
        model = Review
        fields = '__all__'
```

```python
#in accounts/forms.py
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta():
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')
```



##### URL

```python
#in urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.password, name='password'),
    path('<str:username>/', views.profile ,name='profile'),
]
#등등...
```



외 CRUD기능을 구현했습니다.

##### Signup

```python
#in views.py
from django.shortcuts import redirect, render
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm,
    PasswordChangeForm
)
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import *
from django.contrib.auth.models import User
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import *
# Create your views here.
# path('signup/', views.signup, name='signup'),
#     path('login/', views.login, name='login'),
#     path('logout/', views.logout, name='logout'),
#     path('delete/', views.delete, name='delete'),
#     path('update/', views.update, name='update'),
#     path('password/', views.password, name='password'),
#     path('<str:username>/', views.profile ,name='profile'),

@require_http_methods(['GET','POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('community:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('community:index')
    else:
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('community:index')
    if request.method == 'POST':
        #1
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            #2
            return redirect(request.GET.get('next') or 'community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

@require_POST
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

@require_POST
def delete(request):
    request.user.delete()
    return redirect('accounts:login')

@login_required
@require_http_methods(['GET','POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', request.user.username)
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
@require_http_methods(['GET','POST'])
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/password.html', context)

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    context = {
        'user' : user,
    }
    return render(request, 'accounts/profile.html', context)
```

모든 기능을 구현하는데 성공했습니다.



구현한 것 : 

- community/ 에서의 CRUD기능
- 로그인기능과 로그인을 하였을때, 하지 않았을 때의 차이점 구현 
- 로그인을 했을 때 수정, 삭제가 가능하게 하는 기능 구현 
- account 의 생성과 삭제 수정 구현



문제점 : 

- 자바스크립트를 모르기 때문에 구현할 수 없는것이 너무 많다...
- 누가 저장하였는지를 남기는 것을 못했다(만든사람만 삭제하게끔 구현을 못함) // 민규님의 좋은 방법을 get하였습니다!