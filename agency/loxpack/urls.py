from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name='loxpack-home'),
    path('about/', views.about, name='loxpack-about'),
    path('property/<int:pk>/', views.pproperty, name='loxpack-property'),
    path('forsale/', views.sale, name='loxpack-sale'),
    path('forrent/', views.rent, name='loxpack-rent'),
    path('contact/', views.contact, name='loxpack-contact'),
    #path('email/', views.emailView, name='email'),
    #path('success/', views.successView, name='success'),
]