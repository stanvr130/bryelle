
from django.urls import path
from user.views import UserHomeView, UserSchoolView,UserVlogView
urlpatterns = [
    path('home/', UserHomeView.as_view(), name='home'),
    path('Calm/', UserSchoolView.as_view(), name='school'),
    path('cool/', UserVlogView.as_view(), name ='vlog'),
    
]

