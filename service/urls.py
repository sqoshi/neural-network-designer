"""neural-network-designer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import RedirectView
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', views.index, name='index'),
                  path('register/', views.sign_up, name='register'),
                  path("logout", views.logout_request, name="logout"),
                  path("login/", views.login_request, name="login"),
                  path("nnb/search/", views.search_nnb, name="search-nnb"),
                  path("nnb/configure/", views.create_nnb, name="create-nnb"),
                  path("nnb/<int:nnb_id>", views.load_nnb, name="nnb"),
                  url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
                  path('graph/<int:graph_id>', views.grafico, name='graph'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
