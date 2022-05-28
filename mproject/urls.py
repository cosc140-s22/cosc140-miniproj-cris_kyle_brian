"""mproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path, include, reverse_lazy
from learnES import views 
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

from learnES.views import welcome, lessons, base, start, detail, submit, thanks, create_review


def root_redirect(request):
  return redirect(reverse_lazy('welcome'))
  



urlpatterns = [
path('',root_redirect),       
path('admin/', admin.site.urls),
path('welcome', welcome, name='welcome'),
path('login/', auth_views.LoginView.as_view(), name='login'),
path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
path('lessons/', lessons, name='lessons'),
path('lessons/<int:lesson_pk>/start/', start, name='lesson-start'),
path('lessons/<int:lesson_pk>/submit/', submit, name='lesson-submit'),
path('lessons/<int:lesson_pk>/thanks/', thanks, name='lesson-thanks'),
path('lessons/<int:lesson_pk>/', detail, name='lesson-detail'),
path('lessons/<int:lesson_pk>/review/', create_review, name='createreview')
# just do pk or wiat ill just change the function
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)