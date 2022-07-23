from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    
    path('login',views.login_user,name='login'),
    path('register',views.Register,name='register'),
    path('logout',views.logout_user,name='logout'),
    # path('mail',views.mail,name='mail'),
    
    
    path('profile',views.profile,name='profile'),
    path('delete',views.delete_user,name='delete'),
    
    
    path('tosolve/<int:id>',views.to_be_solved,name='to_be_solved'),
    path('ques/<int:id>',views.questions,name='questions'),
    path('view/<int:id>',views.view_code,name='view_code'),   
    path('review/<int:id>',views.solved,name='solved'),
] 