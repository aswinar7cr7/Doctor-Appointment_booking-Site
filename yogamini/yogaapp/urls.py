from django.urls import path
from .import views

urlpatterns=[
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('add',views.addcontact,name='add'), 
    path('accounts/forgot', views.forgot_password, name='forgot'),
    path('logout',views.logout_view,name='logout'),
    path('accounts/resetpassword',views.resetpassword, name='reset'),
    path('bookings',views.views_bookings,name='bookings'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('update_booking/<int:booking_id>/', views.update_booking, name='update_booking'),  # New URL for update



    

]