from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('', GeneralHome.as_view(), name='index'),
    path('', NewsHome.as_view(), name='post'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('employees/', SotrHome.as_view(), name='employees'),
    path('signupuser/', SignupUser.as_view(), name='signupuser'),
    path('loginuser/', LoginUser.as_view(), name='loginuser'),
    path('logout/', auth_views.LogoutView.as_view(template_name='department/logout.html'), name='logout'),

    path('timetables/', TableHome.as_view(), name='timetables'),

    path('timetables/<int:pk>',
         Wrapper.as_view(queryset=Articles.objects.all().order_by("time_of_day").order_by("day_of_week"),
                         template_name="department/wrapper.html")),
]
