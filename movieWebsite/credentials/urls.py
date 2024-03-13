from django.urls import path

from credentials import views

app_name='credentials'

urlpatterns = [
   path('register/',views.register,name='register'),
   path('login/',views.login,name='login'),
   path('logout/',views.logout,name='logout'),
   path('profile/<int:id>/',views.profile,name='profile'),
   path('update/<int:id>/',views.update,name='update'),
]