"""entrepreneurideas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from pages.views import home_view, test_view, about_view, contact_view
from entrusers.views import entr_users_detail_view, entr_users_create_view
from partusers.views import partner_users_create_view, partner_users_detail_view
from django.views.generic import TemplateView

urlpatterns = [
    # Admin section:
    path('admin/', admin.site.urls),

    # Home section
    path('', home_view, name='home'),
    # path('home/', home_view, name='home'),
    # path('home/', TemplateView.as_view(template_name='bootstrap/example.html'), name='home'),

    # Testing URLs
    path('testpage/', test_view, name='test_view'),

    # Home section URL
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),

    # Login functionality URLS (Login functionality is provided by django.authentication):
    # path('login/', TemplateView.as_view(template_name='login.html'), name='loginView'),
    # path('loginSuccess/', TemplateView.as_view(template_name='loginsuccess.html'), name='loginSuccessView'),

    # Contact section URLS:
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    # path('contact/', contact_view, name='contact_view'),

    # About section URLS:
    path('about/', about_view, name='aboutView'),

    # Entrepreneur Users section URLS:
    path('entrusers/', entr_users_detail_view, name='entrusersdetailview'),
    path('createentruser/', entr_users_create_view, name='entruserscreateview'),

    # Partner Users section URLS:
    path('partusers/', partner_users_detail_view, name='partusersdetailview'),
    path('createpartuser/', partner_users_create_view, name='partuserscreateview'),

    # Authorization section (login)
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', TemplateView.as_view(template_name='login.html'), name='loginView'),
    path('accounts/logout/', TemplateView.as_view(template_name='logged_out.html'), name='logoutView'),
    # path('loginSuccess/', TemplateView.as_view(template_name='loginsuccess.html'), name='loginSuccessView'),
    # URLs provided by "auth":
    #     accounts/login/ [name='login']
    #     accounts/logout/ [name='logout']
    #     accounts/password_change/ [name='password_change']
    #     accounts/password_change/done/ [name='password_change_done']
    #     accounts/password_reset/ [name='password_reset']
    #     accounts/password_reset/done/ [name='password_reset_done']
    #     accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    #     accounts/reset/done/ [name='password_reset_complete']
    # HAMMER TIME:
                  # What is this :
                  # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) ?

    # Ideas section
    path('ideas/', TemplateView.as_view(template_name='fillIdea.html'), name='ideaFormView'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
